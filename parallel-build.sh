#!/bin/bash

# =============================================================================
# Parallel Website Builder
# Startet mehrere Claude-Sessions parallel für Website-Erstellung
# =============================================================================

set -e

# Konfiguration
MAX_PARALLEL=${MAX_PARALLEL:-5}       # Max parallele Prozesse (default: 5)
LOG_DIR="./build-logs"                 # Log-Verzeichnis
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

# Farben für Output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Log-Verzeichnis erstellen
mkdir -p "$LOG_DIR"

# =============================================================================
# Hilfe anzeigen
# =============================================================================
show_help() {
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "Options:"
    echo "  -f, --file FILE       CSV-Datei mit Firmen (Format: name,url)"
    echo "  -a, --airtable        Firmen aus Airtable laden (wo 'Seite erstellt' = false)"
    echo "  -n, --count N         Anzahl Websites zu erstellen (default: alle)"
    echo "  -p, --parallel N      Max parallele Prozesse (default: 5)"
    echo "  -d, --dry-run         Nur anzeigen, nicht ausführen"
    echo "  -h, --help            Diese Hilfe anzeigen"
    echo ""
    echo "Beispiele:"
    echo "  $0 -f firmen.csv -p 10           # 10 parallel aus CSV"
    echo "  $0 -a -n 5 -p 3                   # 5 aus Airtable, 3 parallel"
    echo ""
}

# =============================================================================
# Firmen aus CSV laden
# =============================================================================
load_from_csv() {
    local file=$1
    if [[ ! -f "$file" ]]; then
        echo -e "${RED}Fehler: CSV-Datei '$file' nicht gefunden${NC}"
        exit 1
    fi

    # CSV lesen (überspringe Header falls vorhanden)
    tail -n +2 "$file" 2>/dev/null || cat "$file"
}

# =============================================================================
# Firmen aus Airtable laden (via Claude)
# =============================================================================
load_from_airtable() {
    local count=${1:-100}
    echo -e "${BLUE}Lade Firmen aus Airtable...${NC}"

    # Claude aufrufen um Airtable zu querien
    claude --print --output-format json "
    Rufe mcp__airtable__list_records auf mit:
    - baseId: app4j0YLgGsYe1luA
    - tableId: tblNQpZPxQleuajZc
    - filterByFormula: NOT({Seite erstellt})
    - maxRecords: $count

    Gib NUR eine CSV-Liste zurück im Format:
    firmenname,website-url

    Keine Erklärungen, nur die CSV-Daten. Ein Eintrag pro Zeile.
    Firmenname in lowercase, Leerzeichen durch Bindestriche ersetzen.
    " 2>/dev/null | grep -E '^[a-z0-9-]+,https?://'
}

# =============================================================================
# Eine Website bauen (wird im Hintergrund ausgeführt)
# =============================================================================
build_website() {
    local name=$1
    local url=$2
    local log_file="$LOG_DIR/${name}_${TIMESTAMP}.log"

    echo -e "${BLUE}[START]${NC} $name → $url"
    echo "Log: $log_file"

    # Claude mit /build-website Command starten
    if claude --print "/build-website $name $url" > "$log_file" 2>&1; then
        echo -e "${GREEN}[DONE]${NC} $name ✓"
        return 0
    else
        echo -e "${RED}[FAIL]${NC} $name ✗ (siehe Log)"
        return 1
    fi
}

# =============================================================================
# Parallele Ausführung mit Job-Kontrolle
# =============================================================================
run_parallel() {
    local firms=("$@")
    local running=0
    local completed=0
    local failed=0
    local total=${#firms[@]}

    echo ""
    echo -e "${YELLOW}═══════════════════════════════════════════════════════${NC}"
    echo -e "${YELLOW}  Parallel Website Builder - $total Websites${NC}"
    echo -e "${YELLOW}  Max parallel: $MAX_PARALLEL${NC}"
    echo -e "${YELLOW}═══════════════════════════════════════════════════════${NC}"
    echo ""

    # Jobs starten
    for firm in "${firms[@]}"; do
        # Warten wenn max parallele erreicht
        while [[ $(jobs -r | wc -l) -ge $MAX_PARALLEL ]]; do
            sleep 5
        done

        # Firma und URL extrahieren
        local name=$(echo "$firm" | cut -d',' -f1 | tr -d ' ')
        local url=$(echo "$firm" | cut -d',' -f2 | tr -d ' ')

        if [[ -n "$name" && -n "$url" ]]; then
            # Im Hintergrund starten
            build_website "$name" "$url" &
        fi
    done

    # Auf alle Jobs warten
    echo ""
    echo -e "${BLUE}Warte auf Abschluss aller Jobs...${NC}"
    wait

    # Ergebnisse zusammenfassen
    echo ""
    echo -e "${YELLOW}═══════════════════════════════════════════════════════${NC}"
    echo -e "${GREEN}  Fertig!${NC}"
    echo -e "${YELLOW}  Logs: $LOG_DIR/${NC}"
    echo -e "${YELLOW}═══════════════════════════════════════════════════════${NC}"
}

# =============================================================================
# Main
# =============================================================================
main() {
    local source=""
    local count=""
    local dry_run=false
    local firms=()

    # Argumente parsen
    while [[ $# -gt 0 ]]; do
        case $1 in
            -f|--file)
                source="file"
                csv_file="$2"
                shift 2
                ;;
            -a|--airtable)
                source="airtable"
                shift
                ;;
            -n|--count)
                count="$2"
                shift 2
                ;;
            -p|--parallel)
                MAX_PARALLEL="$2"
                shift 2
                ;;
            -d|--dry-run)
                dry_run=true
                shift
                ;;
            -h|--help)
                show_help
                exit 0
                ;;
            *)
                echo -e "${RED}Unbekannte Option: $1${NC}"
                show_help
                exit 1
                ;;
        esac
    done

    # Firmen laden
    if [[ "$source" == "file" ]]; then
        mapfile -t firms < <(load_from_csv "$csv_file")
    elif [[ "$source" == "airtable" ]]; then
        mapfile -t firms < <(load_from_airtable "$count")
    else
        echo -e "${RED}Fehler: Keine Quelle angegeben (-f oder -a)${NC}"
        show_help
        exit 1
    fi

    # Anzahl begrenzen wenn angegeben
    if [[ -n "$count" && ${#firms[@]} -gt $count ]]; then
        firms=("${firms[@]:0:$count}")
    fi

    if [[ ${#firms[@]} -eq 0 ]]; then
        echo -e "${YELLOW}Keine Firmen gefunden.${NC}"
        exit 0
    fi

    echo -e "${GREEN}Gefunden: ${#firms[@]} Firmen${NC}"

    # Dry-run: nur anzeigen
    if [[ "$dry_run" == true ]]; then
        echo ""
        echo "Würde folgende Websites erstellen:"
        for firm in "${firms[@]}"; do
            echo "  - $firm"
        done
        exit 0
    fi

    # Parallel ausführen
    run_parallel "${firms[@]}"
}

main "$@"

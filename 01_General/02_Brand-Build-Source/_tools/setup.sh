#!/bin/bash
# Khôi phục môi trường build (các script hardcode đường dẫn /tmp/...). Chạy: bash _tools/setup.sh
set -e
HERE="$(cd "$(dirname "$0")" && pwd)"; WS="$(dirname "$HERE")"
python3 -m venv /tmp/brandenv && /tmp/brandenv/bin/pip install -q -r "$HERE/requirements.txt"
mkdir -p /tmp/brandbuild /tmp/dk /tmp/trace /tmp/fonts /tmp/kit_out
cp "$HERE"/brandbuild/* /tmp/brandbuild/; cp "$HERE"/dk/* /tmp/dk/; cp "$HERE"/trace_data/* /tmp/trace/
cp "$WS/brandkit/03_Typography/fonts/PlusJakartaSans[wght].ttf" /tmp/fonts/PlusJakartaSans.ttf
cp "$WS/brandkit/03_Typography/fonts/Inter[opsz,wght].ttf" /tmp/fonts/Inter.ttf
# render PDF -> PNG để xem lại (Swift PDFKit): /tmp/pdfwork/ex.swift (xem CLAUDE.md)
echo "OK. Dùng: /tmp/brandenv/bin/python /tmp/brandbuild/build_xxx.py"

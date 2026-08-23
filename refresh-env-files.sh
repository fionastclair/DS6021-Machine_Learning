#!/usr/bin/env bash
# Regenerate requirements.txt from uv.lock, so pip and conda students get the
# same versions as uv students. Run this after any dependency change.
set -euo pipefail
cd "$(dirname "$0")"

uv lock
uv export --no-hashes --no-emit-project --format requirements-txt \
  | sed 's|^#    uv export.*|#    ./refresh-env-files.sh|' \
  > requirements.txt

echo "requirements.txt updated ($(grep -cvE '^\s*#|^$' requirements.txt) packages)"
echo "environment.yml reads requirements.txt, so it needs no change."

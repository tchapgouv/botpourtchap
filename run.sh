#!/bin/sh

cat <<EOF > pantalaimon.conf
[local-matrix]
Homeserver = $MATRIX_HOME_SERVER
ListenAddress = localhost
ListenPort = $PANTALAIMON_PORT
DebugEncryption = True
DropOldKeys = True
UseKeyring = False
HistoryFetchDelay = 500
IgnoreVerification = True
EOF

pantalaimon -c pantalaimon.conf --log-level debug & python bot.py

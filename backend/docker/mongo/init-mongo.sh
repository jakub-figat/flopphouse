set -e

mongo <<EOF
use $MONGODB_INITDB_DATABASE

db.users.createIndex({ username: 1 }, { unique: true })
db.users.createIndex({ email: 1 }, { unique: true })

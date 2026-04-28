find . -type f ! -path './third_party/*' -size -5M \
-exec grep -Hn -C2 'TimeoutError' {} + \
| grep -E '^[^:]+:[0-9]+:.*TimeoutError'


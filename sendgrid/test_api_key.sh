for var in `cat .env`; do
    export ${var}
done

# Look for a 202 response code!
curl -i --request POST \
--url https://api.sendgrid.com/v3/mail/send \
--header "Authorization: Bearer ${SENDGRID_API_KEY}" \
--header 'Content-Type: application/json' \
--data '{"personalizations": [{"to": [{"email": "recipient@example.com"}]}],"from": {"email": "sendeexampexample@example.com"},"subject": "Hello, World!","content": [{"type": "text/plain", "value": "Howdy!"}]}'

echo

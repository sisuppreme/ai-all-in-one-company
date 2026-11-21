# Example 1 — Manual cert and calendar renewal

## Before

The site goes live after a one-off command on the server:

```bash
sudo certbot certonly --standalone -d example.com
```

The launch checklist gains a line: "Renew the certificate before it expires in March." No systemd timer is enabled, no reload hook exists, and renewal has never been tested. Three months later the certificate expires on a weekend and the site serves a browser warning until someone re-runs the command by hand.

## After

The certificate is issued through the web-server plugin with the renewal timer enabled and a deploy hook that reloads the server:

```bash
sudo certbot --nginx -d example.com
sudo systemctl enable --now certbot.timer
# /etc/letsencrypt/renewal/example.com.conf contains:
# deploy_hook = systemctl reload nginx
sudo certbot renew --dry-run
```

The dry-run passes at setup, an expiry alert is set 30 days ahead as a backstop, and the served certificate's dates are checked against the on-disk certificate after the first renewal.

Note: corrects DO-221, DO-226, DO-227 — automated issuance, unattended renewal with reload hook, renewal proven by dry-run.

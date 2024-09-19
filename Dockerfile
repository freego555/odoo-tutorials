FROM odoo:17.0-20240912

COPY ./addons /mnt/extra-addons
COPY ./addon-examples /mnt/extra-addons

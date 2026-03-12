# Premium E-Commerce Project (Starter)

Yahi project hai ✅

Is commit mein documentation ke saath actual Django starter project scaffold add kiya gaya hai jisme:

- Custom user model with roles (customer/admin/delivery)
- Product/category models
- Coupon + order + order items + order status workflow
- Delivery assignment + live location pings model
- Notification model
- Django admin registrations
- Health endpoint (`/health/`)

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open:

- Admin: http://127.0.0.1:8000/admin/
- Health: http://127.0.0.1:8000/health/

## Notes

- Default DB is SQLite for fast local setup.
- Production ke liye MySQL config `config/settings.py` mein update karein.

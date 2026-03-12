# Premium E-Commerce Website System — Final Requirement Document

## 1) Project Overview

This project is a premium full-stack e-commerce web application inspired by modern quick-commerce platforms.

The system includes three major panels:

1. **Customer Panel** (User side)
2. **Admin Panel** (Management dashboard)
3. **Delivery Boy Panel** (Delivery dashboard)

The platform supports:

- Real-time order updates
- Inventory management
- Notifications
- Coupon eligibility and redemption
- Live delivery tracking

The UI must be premium, modern, and fully responsive across desktop, tablet, and mobile devices.

---

## 2) Technology Stack

### Frontend

- HTML5
- CSS3
- JavaScript
- Bootstrap and/or Tailwind CSS
- Responsive design principles

### Backend

- Python
- Django framework

### Database

- MySQL

### Real-Time Tracking

- Django Channels (WebSockets) **or** Firebase Realtime Database

### Maps Integration

- Google Maps API for live delivery tracking

---

## 3) Customer Panel (User Side)

### 3.1 Authentication

- User registration
- User login
- Phone OTP-based password reset
- Profile management

### 3.2 Shopping Features

- Product browsing
- Product search and filters
- Product detail page
- Add to cart
- Remove from cart

### 3.3 Wishlist

- Add product to wishlist
- Remove product from wishlist
- Wishlist listing page

### 3.4 Cart and Checkout

- View cart items
- Update quantities
- Checkout page
- Apply coupon

### 3.5 Coupon System (Customer View)

Coupons are created by admin.

**Example coupon:**

- Minimum order: ₹2000
- Discount: ₹300 OFF

**Cart logic:**

- If cart total is ₹1700, display:
  - `Add ₹300 more to unlock ₹300 OFF coupon`
- If cart total is ≥ ₹2000, coupon becomes available for application.

### 3.6 Orders

Customers can:

- Place orders
- View order history
- Track order status

**Order statuses:**

1. Order Placed
2. Packing
3. Ready for Delivery
4. Out for Delivery
5. Delivered

### 3.7 Notifications

Customers receive notifications for:

- Order placed
- Order shipped / packed
- Delivery boy assigned
- Order delivered
- New coupon offers

### 3.8 Live Delivery Tracking

Customers can see:

- Delivery boy name
- Phone number
- Estimated delivery time
- Live location on map

---

## 4) Admin Panel (Premium Dashboard)

Admin dashboard must look professional and include analytics + management tools.

### 4.1 Dashboard Overview

Admin can view:

- Total users
- Total orders
- Total products
- Total revenue
- Active deliveries

Analytics include:

- Daily sales graph
- Monthly sales graph
- Top-selling products

### 4.2 Product Management

Admin can:

- Add products
- Edit products
- Delete products
- Upload product images
- Manage product categories

### 4.3 Inventory Management

Admin can:

- Update product stock
- Track inventory
- Receive low-stock alerts
- Auto-mark products as **Out of Stock**

### 4.4 Order Management

Admin can:

- View all orders
- View order details
- Update order statuses

**Order workflow:**

1. Order Placed
2. Packing
3. Ready for Delivery
4. Out for Delivery
5. Delivered

### 4.5 Delivery Boy Management

Admin can:

- Add delivery boys
- Edit delivery boys
- Activate/deactivate delivery boys
- Assign delivery boys to orders

### 4.6 Coupon Management

Admin can:

- Create coupon
- Edit coupon
- Delete coupon

**Coupon fields:**

- Coupon code
- Minimum order amount
- Discount amount
- Expiry date

When a coupon is created, users receive a notification.

### 4.7 User Management

Admin can:

- View user details
- View user orders
- Block/unblock users
- Trigger password reset

Admin must **not** be able to view user passwords.

---

## 5) Delivery Boy Panel

Delivery dashboard must be mobile friendly.

### 5.1 Authentication

- Login using phone + password
- Forgot password via OTP

### 5.2 Assigned Orders

Delivery boy can view:

- Customer name
- Delivery address
- Customer phone number
- Order details

### 5.3 Delivery Actions

Delivery boy can:

- Accept order
- Start delivery
- Mark order as delivered

### 5.4 Order Status Updates

Delivery panel updates:

- Out for Delivery
- Delivered

Status changes must reflect in admin and customer panels in real time.

### 5.5 Live Location Sharing

Delivery device sends GPS location updates.

Location is visible to:

- Customer
- Admin

---

## 6) Notification System

System-generated notifications are sent for:

- Order placed
- Order packed
- Order ready for delivery
- Delivery boy assigned
- Order delivered
- New coupon offer

---

## 7) Security Requirements

- Password hashing (no plain-text password storage)
- OTP verification for password reset
- Secure login and authentication flow
- Role-based access controls
- Admin cannot view user passwords

---

## 8) Premium UI/UX Design Requirements

The experience should be premium and modern.

Design guidelines:

- Clean layout and visual hierarchy
- Smooth micro-animations
- High-quality product imagery
- Elegant typography
- Soft shadows and rounded cards
- Responsive design across mobile/tablet/desktop
- Dashboard cards and charts with polished styling

Admin UI should resemble modern SaaS dashboards.
Delivery panel should be optimized for mobile workflows.

---

## 9) Core System Modules

1. User System
2. Product System
3. Cart System
4. Wishlist System
5. Coupon System
6. Inventory System
7. Order System
8. Delivery System
9. Notification System
10. Analytics System

---

## 10) Final Goal

Build a modern quick-commerce platform where:

- Customers can discover and purchase products easily
- Admins can operate and monitor the business effectively
- Delivery boys can complete assigned deliveries efficiently
- Orders are trackable in real time end-to-end

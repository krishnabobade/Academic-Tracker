# 🎓 Academic Portal — Full-Stack Learning Management System

A production-ready, three-tier academic management web application with role-based authentication, real-time assignment countdown timers, automated email reminders, and student performance analytics.

---

## 📐 Architecture

```
┌─────────────────────────────────────────────────────────┐
│  PRESENTATION LAYER (Frontend)                          │
│  HTML5 + CSS3 + Bootstrap 5 + Vanilla JS ES6+           │
│  Single-Page Application served by Express static       │
├─────────────────────────────────────────────────────────┤
│  APPLICATION LAYER (Backend)                            │
│  Node.js v18+ / Express.js / JWT / bcrypt               │
│  RESTful API, MVC pattern, modular services             │
├─────────────────────────────────────────────────────────┤
│  DATA LAYER (Database)                                  │
│  MySQL 8.0 — fully normalised 3NF                       │
│  Connection pooling via mysql2/promise                  │
└─────────────────────────────────────────────────────────┘
```

---

## 📁 Project Structure

```
academic-portal/
├── .env.example                  # Environment template
├── logs/                         # Auto-created log directory
├── uploads/                      # Student submission files
│
├── database/
│   ├── schema.sql                # Table definitions + indexes
│   └── seed.sql                  # Demo data
│
├── frontend/
│   ├── index.html                # SPA shell
│   ├── css/style.css             # Full custom stylesheet
│   └── js/
│       ├── api.js                # Fetch API client
│       ├── utils.js              # Toast, Modal, Countdown
│       ├── auth.js               # Login/register UI
│       ├── teacher.js            # Teacher dashboard
│       ├── student.js            # Student dashboard
│       └── app.js                # Root controller
│
└── backend/
    ├── server.js                 # Express entry point
    ├── package.json
    ├── config/
    │   └── database.js           # MySQL connection pool
    ├── middleware/
    │   ├── auth.js               # JWT authenticate + authorise
    │   ├── audit.js              # Audit logging
    │   ├── upload.js             # Multer file uploads
    │   └── errorHandler.js       # Global error handler
    ├── services/                 # Business logic (no HTTP)
    │   ├── authService.js
    │   ├── assignmentService.js
    │   ├── announcementService.js
    │   └── emailService.js       # Nodemailer + cron scheduler
    ├── controllers/              # Route handlers
    │   ├── authController.js
    │   ├── assignmentController.js
    │   └── announcementController.js
    ├── routes/
    │   ├── auth.js
    │   ├── assignments.js
    │   └── announcements.js
    ├── utils/
    │   ├── jwt.js
    │   ├── logger.js             # Winston
    │   └── response.js
    └── tests/
        └── unit.test.js          # Jest unit tests
```

---

## 🚀 Setup & Installation

### Prerequisites
- Node.js v18 or higher
- MySQL 8.0
- npm v9+

### 1. Clone and install
```bash
git clone <repository-url>
cd academic-portal/backend
npm install
```

### 2. Configure environment
```bash
cp .env.example .env
# Edit .env with your MySQL credentials and SMTP settings
```

### 3. Set up database
```bash
mysql -u root -p < database/schema.sql
mysql -u root -p < database/seed.sql
```

### 4. Start the server
```bash
# Development (with auto-restart)
npm run dev

# Production
npm start
```

The application will be available at **http://localhost:3000**

---

## 🔐 Environment Configuration

| Variable | Description | Default |
|----------|-------------|---------|
| `PORT` | Server port | 3000 |
| `NODE_ENV` | Environment | development |
| `DB_HOST` | MySQL host | localhost |
| `DB_PORT` | MySQL port | 3306 |
| `DB_NAME` | Database name | academic_portal |
| `DB_USER` | MySQL user | root |
| `DB_PASSWORD` | MySQL password | — |
| `JWT_SECRET` | JWT signing secret (min 32 chars) | — |
| `JWT_EXPIRES_IN` | Token expiry | 8h |
| `SMTP_HOST` | SMTP server | smtp.gmail.com |
| `SMTP_PORT` | SMTP port | 587 |
| `SMTP_USER` | SMTP username | — |
| `SMTP_PASS` | SMTP app password | — |
| `EMAIL_FROM` | Sender display | Academic Portal |
| `UPLOAD_DIR` | File upload directory | uploads |
| `MAX_FILE_SIZE_MB` | Max upload size (MB) | 10 |

---

## 🧪 Running Tests

```bash
cd backend
npm test              # Run all tests with coverage
npm run test:watch    # Watch mode
```

Tests cover:
- JWT sign/verify + tamper detection + expiry
- bcrypt password hashing
- Deadline status logic
- Countdown urgency colour logic
- Performance percentage calculation
- Response utility helpers
- Auth middleware (authenticate + authorise)

---

## 📡 API Reference

### Authentication
| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| POST | `/api/auth/register` | — | Register new user |
| POST | `/api/auth/login` | — | Login, returns JWT |
| GET | `/api/auth/profile` | JWT | Get current user |

### Assignments
| Method | Endpoint | Auth | Role |
|--------|----------|------|------|
| GET | `/api/assignments` | JWT | Both |
| GET | `/api/assignments/:id` | JWT | Both |
| POST | `/api/assignments` | JWT | Teacher |
| PUT | `/api/assignments/:id` | JWT | Teacher |
| DELETE | `/api/assignments/:id` | JWT | Teacher |
| GET | `/api/assignments/teacher/mine` | JWT | Teacher |
| GET | `/api/assignments/teacher/summary` | JWT | Teacher |
| GET | `/api/assignments/:id/submissions` | JWT | Teacher |
| POST | `/api/assignments/:id/submit` | JWT | Student |
| GET | `/api/assignments/student/my-submissions` | JWT | Student |
| GET | `/api/assignments/student/performance` | JWT | Student |

### Announcements
| Method | Endpoint | Auth | Role |
|--------|----------|------|------|
| GET | `/api/announcements` | JWT | Both |
| GET | `/api/announcements/:id` | JWT | Both |
| POST | `/api/announcements` | JWT | Teacher |
| PUT | `/api/announcements/:id` | JWT | Teacher |
| DELETE | `/api/announcements/:id` | JWT | Teacher |

---

## 🔒 Security Checklist

- [x] JWT-based stateless authentication (HS256, configurable expiry)
- [x] bcrypt password hashing (12 salt rounds)
- [x] SQL injection prevention via parameterised queries throughout
- [x] Input validation with express-validator (server-side)
- [x] Helmet.js security headers (CSP, X-Frame-Options, etc.)
- [x] Rate limiting (100 req/15min globally; 20 req/15min on auth)
- [x] CORS restricted to configured origin
- [x] File upload validation (MIME type + size)
- [x] Audit logging for all login attempts and API access
- [x] Ownership verification before assignment/announcement modification
- [x] HTTP 403 Forbidden for role violations
- [x] No raw string interpolation in any SQL queries
- [x] Sensitive fields stripped from audit log
- [x] .env excluded from version control via .gitignore

---

## 📧 Email Reminder System

The scheduler runs every **30 minutes** via `node-cron` and sends email reminders to students who have **not yet submitted** assignments due in:
- **48 hours**
- **24 hours**

Emails include the assignment title, subject, exact deadline, and the student's name. Email failures are logged but never block the main request thread.

To enable, configure SMTP credentials in `.env`.

---

## 🚀 Deployment Guide

### Production environment

1. Set `NODE_ENV=production` in `.env`
2. Use a process manager:
   ```bash
   npm install -g pm2
   pm2 start backend/server.js --name "academic-portal"
   pm2 startup && pm2 save
   ```
3. Configure Nginx reverse proxy:
   ```nginx
   server {
     listen 80;
     server_name yourdomain.com;
     location / {
       proxy_pass http://localhost:3000;
       proxy_http_version 1.1;
       proxy_set_header Upgrade $http_upgrade;
       proxy_set_header Connection 'upgrade';
       proxy_set_header Host $host;
       proxy_cache_bypass $http_upgrade;
     }
   }
   ```
4. Add SSL/TLS via Let's Encrypt:
   ```bash
   certbot --nginx -d yourdomain.com
   ```

---

## 🔮 Future-Ready Design

The modular architecture supports easy addition of:
- **WebSocket notifications** — add `socket.io` to `server.js`, emit events from services
- **Grading system** — extend submissions table with `grade` + `feedback` columns
- **Analytics dashboard** — add `/api/analytics` routes, connect to Chart.js
- **Google Calendar** — integrate in `emailService.js` using Google Calendar API
- **Multi-institution** — add `institution_id` FK to users + assignments tables

---

## 📖 Demo Credentials

After running `seed.sql`:

| Role | Email | Password |
|------|-------|----------|
| Teacher | teacher@demo.com | Password123! |
| Student | student1@demo.com | Password123! |
| Student | student2@demo.com | Password123! |

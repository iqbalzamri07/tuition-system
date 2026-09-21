This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app).

## Architecture

```
                    Browser
                       │
                       ▼
              ┌─────────────────┐
              │    Next.js      │
              │   TypeScript    │
              │ Tailwind/shadcn │
              └────────┬────────┘
                       │ REST API
                       ▼
              ┌─────────────────┐
              │     FastAPI     │
              │     Python      │
              ├─────────────────┤
              │ Authentication  │
              │ Students        │
              │ Classes         │
              │ Attendance      │
              │ Homework        │
              │ Payments        │
              │ Analytics       │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │   PostgreSQL    │
              └─────────────────┘
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
        Object Storage         AI API
       homework/files       AI analysis
```

## Tech Stack

| Layer          | Technology                              | Why                                     |
| -------------- | --------------------------------------- | --------------------------------------- |
| Frontend       | **Next.js + TypeScript**                | Great for dashboard/web app             |
| UI             | **Tailwind CSS + shadcn/ui**            | Fast to build a clean admin UI          |
| Backend        | **FastAPI + Python**                    | Excellent if you want AI features later |
| Database       | **PostgreSQL**                          | Reliable relational DB                  |
| ORM            | **SQLModel / SQLAlchemy**               | Good fit with FastAPI                   |
| Authentication | **JWT / HTTP-only cookies**             | Simple single-teacher authentication    |
| File storage   | **S3-compatible storage**               | Homework, receipts, documents           |
| Charts         | **Recharts**                            | Student performance analytics           |
| PDF            | **ReportLab** or browser PDF generation | Receipts/reports                        |
| Notifications  | **WhatsApp/Email later**                | Don't need initially                    |
| Deployment     | **Docker + Ubuntu VPS**                 | Easy deployment and backup              |
| Reverse proxy  | **Caddy**                               | Easier HTTPS setup                      |
| AI             | **OpenAI API / local LLM later**        | Student analysis/report generation      |

## Project Structure

### Backend

```
backend/
├── app/
│   ├── main.py
│   ├── models/
│   │   ├── student.py
│   │   ├── parent.py
│   │   ├── class.py
│   │   ├── attendance.py
│   │   ├── homework.py
│   │   ├── exam.py
│   │   └── payment.py
│   │
│   ├── api/
│   │   ├── students.py
│   │   ├── classes.py
│   │   ├── attendance.py
│   │   ├── homework.py
│   │   ├── payments.py
│   │   └── analytics.py
│   │
│   ├── services/
│   │   ├── attendance_service.py
│   │   ├── payment_service.py
│   │   ├── report_service.py
│   │   └── ai_service.py
│   │
│   └── core/
│       ├── config.py
│       └── security.py
│
└── tests/
```

### Frontend

```
frontend/
├── app/
│   ├── dashboard/
│   ├── students/
│   ├── classes/
│   ├── attendance/
│   ├── homework/
│   ├── payments/
│   ├── reports/
│   └── settings/
│
├── components/
│   ├── ui/
│   ├── students/
│   ├── attendance/
│   └── payments/
│
├── lib/
│   ├── api.ts
│   └── auth.ts
│
└── types/
```

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) to automatically optimize and load [Geist](https://vercel.com/font), a new font family for Vercel.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.

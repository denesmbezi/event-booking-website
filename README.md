# Appointment Scheduler

A Django-based web application for scheduling appointments with email confirmations and PDF generation.

## Features

- **Appointment Booking**: Simple form to book appointments with name, email, phone, date, and time
- **Email Notifications**: Automated email confirmations using Resend
- **PDF Generation**: Generate PDF attachments for appointment details using ReportLab
- **Admin Panel**: Django admin interface for managing bookings and email templates
- **Responsive Design**: Mobile-friendly UI built with Tailwind CSS
- **Docker Support**: Containerized deployment ready

## Tech Stack

- **Backend**: Django 4.2.7
- **Database**: SQLite (development), configurable for production
- **Email Service**: Resend
- **PDF Generation**: ReportLab
- **Frontend**: HTML, Tailwind CSS
- **Deployment**: Docker

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd appointment_scheduler
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (optional, for admin access):
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

   Visit `http://localhost:8000` to access the application.

## Usage

### Booking Appointments

1. Navigate to the home page
2. Fill out the booking form with your details
3. Select preferred date and time
4. Submit the form

### Admin Panel

Access the Django admin at `http://localhost:8000/admin/` to:
- View and manage bookings
- Configure email templates
- Update booking statuses

## Configuration

### Email Settings

Configure Resend API key in your environment or Django settings for email functionality.

### Database

The application uses SQLite by default. For production, configure PostgreSQL or another database in `settings.py`.

## Docker Deployment

1. **Build the Docker image**:
   ```bash
   docker build -t appointment-scheduler .
   ```

2. **Run the container**:
   ```bash
   docker run -p 8000:8000 appointment-scheduler
   ```

The application will be available at `http://localhost:8000`.

## Project Structure

```
appointment_scheduler/
├── appointment_scheduler/     # Main Django project settings
├── bookings/                  # Booking app
│   ├── models.py             # Booking and EmailTemplate models
│   ├── views.py              # View logic
│   ├── templates/            # HTML templates
│   └── migrations/           # Database migrations
├── db.sqlite3                # SQLite database
├── Dockerfile                # Docker configuration
├── requirements.txt          # Python dependencies
├── manage.py                 # Django management script
└── README.md                 # This file
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.
from django.contrib import admin
from .models import Booking, EmailTemplate
from django.core.mail import EmailMessage
from reportlab.pdfgen import canvas
from io import BytesIO
from django.conf import settings

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date', 'time', 'status')
    list_filter = ('status', 'date')
    actions = ['confirm_bookings']

    def confirm_bookings(self, request, queryset):
        for booking in queryset:
            booking.status = 'confirmed'
            booking.save()
            # Generate PDF
            buffer = BytesIO()
            p = canvas.Canvas(buffer)
            p.drawString(100, 750, f"Appointment Confirmation for {booking.name}")
            p.drawString(100, 730, f"Date: {booking.date}")
            p.drawString(100, 710, f"Time: {booking.time}")
            p.drawString(100, 690, f"Email: {booking.email}")
            p.drawString(100, 670, f"Phone: {booking.phone}")
            p.showPage()
            p.save()
            buffer.seek(0)
            # Send email
            email = EmailMessage(
                'Appointment Confirmed',
                'Your appointment has been confirmed. See attached PDF.',
                settings.DEFAULT_FROM_EMAIL,
                [booking.email],
            )
            email.attach('appointment.pdf', buffer.getvalue(), 'application/pdf')
            email.send()
        self.message_user(request, f"{queryset.count()} bookings confirmed and emails sent.")

    confirm_bookings.short_description = "Confirm selected bookings"

@admin.register(EmailTemplate)
class EmailTemplateAdmin(admin.ModelAdmin):
    pass
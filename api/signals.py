from .text_summarizer import run_summarization
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Note, Summary


@receiver(post_save, sender=Note)
def create_summary(sender, instance, created, **kwargs):
    summary = run_summarization(instance.body)
    if created:
        Summary.objects.create(associated_note=instance, summary=summary)

# post_save.connect(create_summary, sender=Note)
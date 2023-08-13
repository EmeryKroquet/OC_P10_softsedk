# models.py

from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _

# Modèle d'utilisateur personnalisé
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(_('Age'))
    can_be_contacted = models.BooleanField(_('Peut être contacté'), default=False)
    can_data_be_shared = models.BooleanField(_('Peut-on partager les données'), default=False)
    # Update the related_name for groups
    groups = models.ManyToManyField(Group, blank=True, related_name='custom_users')

    # Update the related_name for user_permissions
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='custom_users',
    )
# Modèle pour les projets
class Project(models.Model):
    name = models.CharField(_('Nom du projet'), max_length=255)
    description = models.TextField(_('Description du projet'))
    type = models.CharField(_('Type de projet'), max_length=100, choices=(
        ('back-end', 'Back-End'),
        ('front-end', 'Front-End'),
        ('iOS', 'iOS'),
        ('Android', 'Android'),
    ))
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='authored_projects')

    #author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='projects')

# Modèle pour les problèmes (issues)
class Issue(models.Model):
    LOW = 'LOW'
    MEDIUM = 'MEDIUM'
    HIGH = 'HIGH'
    PRIORITY_CHOICES = (
        (LOW, _('Low')),
        (MEDIUM, _('Medium')),
        (HIGH, _('High')),
    )

    BUG = 'BUG'
    FEATURE = 'FEATURE'
    TASK = 'TASK'
    TAG_CHOICES = (
        (BUG, _('Bug')),
        (FEATURE, _('Feature')),
        (TASK, _('Task')),
    )

    title = models.CharField(_('Titre de l\'issue'), max_length=255)
    description = models.TextField(_('Description de l\'issue'))
    status = models.CharField(_('Statut de l\'issue'), max_length=100, default='To Do')
    priority = models.CharField(_('Priorité de l\'issue'), max_length=10, choices=PRIORITY_CHOICES, default=LOW)
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    tag = models.CharField(_('Balise de l\'issue'), max_length=10, choices=TAG_CHOICES, default=BUG)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='issues')

# Modèle pour les commentaires
class Comment(models.Model):
    text = models.TextField(_('Texte du commentaire'))
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments')
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='comments')

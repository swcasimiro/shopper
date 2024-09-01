from django import forms


class ContactForm(forms.Form):  # создание контактной формы, без связи с моделей.
    email = forms.EmailField(
        max_length=255,
        label="<br> Введите вашу почту",
    )
    full_name = forms.CharField(
        max_length=90,
        label="<br> Введите ваше полное имя",
    )
    message = forms.CharField(
        widget=forms.Textarea,
        max_length=555,
        label="<br>",
        initial="Ваше сообщение",
    )



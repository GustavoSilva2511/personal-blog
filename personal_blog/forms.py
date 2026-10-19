from django import forms

INPUT_CLASSES = (
    "w-full rounded-xl border border-slate-300 bg-white px-4 py-2.5 text-slate-900 "
    "placeholder-slate-400 shadow-sm transition focus:border-indigo-500 "
    "focus:outline-none focus:ring-2 focus:ring-indigo-500/30"
)


class BlogPostForm(forms.Form):
    title = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={"class": INPUT_CLASSES, "placeholder": "Título do artigo"}
        ),
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": INPUT_CLASSES + " min-h-48 resize-y",
                "placeholder": "Escreva o conteúdo aqui...",
                "rows": 8,
            }
        )
    )

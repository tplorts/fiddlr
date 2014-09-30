from django.shortcuts import render
from django.views.generic import TemplateView
from fiddlr import settings


class Wiew(TemplateView):
    template = 'base'

    def get_context_data(self, **kwargs):
        context = super(Wiew, self).get_context_data(**kwargs)
        if 'ngScopeVars' in context:
            context['ngScopeInitials'] = {}
            for symbol in context['ngScopeVars']:
                if symbol in context:
                    context['ngScopeInitials'].update({
                        symbol: context[symbol],
                    })
        context.update({
            'isProduction': settings.isProduction,
            'useLESS': not settings.isProduction,
            'GoogleAPIKey': settings.GOOGLE_API_KEY,
        })
        return context

    def get_template_names(self):
        return [self.template + '.djt']

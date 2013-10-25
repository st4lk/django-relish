from django.contrib import messages


class SuccessMessageMixin(object):
    success_message = None

    def get_success_message(self):
        return self.success_message

    def form_valid(self, form):
        if self.get_success_message():
            messages.success(self.request, self.get_success_message())
        return super(SuccessMessageMixin, self).form_valid(form)

    def delete(self, *args, **kwargs):
        if self.get_success_message():
            messages.success(self.request, self.get_success_message())
        return super(SuccessMessageMixin, self).delete(*args, **kwargs)

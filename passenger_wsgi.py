   self.helper = FormHelper()
        self.helper.form_id = "bank_account-form-id"
        self.helper.form_class = "bank_account-form-class"
        self.helper.layout = Layout(
        HTML("""
            <p><strong style="font-size: 18px;">{}</strong></p>
            <hr>
        """.format(_('Add/Update Bank Account'),)),
        BS5Accordion(
            AccordionGroup(_('BANK ACCOUNT MAIN DATA'),
                Row(
                    Column('name', css_class='form-group col-md-12 mb-0'),
                Row(
                    Column('address', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
                ),
                Row(
                    Column('telephone', css_class='form-group col-md-4 mb-0'),
                    Column('fax', css_class='form-group col-md-4 mb-0'),
                    Column('cell', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
                ),
                Row(
                    Column('email', css_class='form-group col-md-4 mb-0'),
                    Column('website', css_class='form-group col-md-6 mb-0'),
                    Column('active_status', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'),
                Row(
                    Column(Field('notes', rows='2'), css_class='form-group col-md-12 mb-0'),
                    css_class='form-row'),
            ),
                HTML('<br>'),
                Submit('save_bank_account', _('Save & Close'), css_class='btn btn-primary fas fa-save'),
                Submit('save_bank_account_new', _('Save & Edit'), css_class='btn btn-primary fas fa-save'),
                Reset('reset', 'Clear', css_class='btn btn-danger'),
                flush=True,
                always_open=True),
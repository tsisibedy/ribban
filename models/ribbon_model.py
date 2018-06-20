# -*- coding: utf-8 -*-

import sys, os
import re
import werkzeug
from odoo import models, fields, api



class Ribban(models.Model):
    _name = 'ribban.active'

    name = fields.Char(string='Ribban name')
    ribbon_text = fields.Char(string='text to display on ribban')

    def open_file_and_edit(self,file_name,text_search,text_replace):
        path = os.path.abspath(__file__)
        dir_path = os.path.dirname(path)
        file_path = str(dir_path).replace('environment_ribbon\models','environment_ribbon\static\src\\xml\\%s'%file_name)
        replace_file = open(file_path, 'r+')
        for line in replace_file:
            if text_search in line:
                replace_text = line
                file_app_switcher_read = open(file_path).read()
                file_app_switcher_read = file_app_switcher_read.replace(replace_text, '\t\t%s'%text_replace+'\n')
                file_app_switcher_write = open(file_path, 'w')
                file_app_switcher_write.write(file_app_switcher_read)
                file_app_switcher_write.close()
                print('Fin d\'activation ribban')

    def active_this_ribban(self):
        file_name_ribban = 'environnement_ribbon.xml'
        text_search_ribban = 'font-weight: bold;">'
        for record in self:
            text_replace_ribban = 'font-weight: bold;">'+ record.ribbon_text +'</div>'
            self.open_file_and_edit(file_name_ribban,text_search_ribban,text_replace_ribban)








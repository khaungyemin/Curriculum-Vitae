from odoo import models, fields


class CurriculumVitaeSimple(models.Model):
    _name = 'curriculum.vitae.simple'
    _description = 'Curriculum Vitae Simple Format'

    name = fields.Char(string="Name")
    nrc = fields.Char(string="NRC")
    date_of_birth = fields.Char(string="Date of Birth")
    place_of_birth = fields.Char(string="Place of Birth")
    nationality = fields.Char(string = "Nationality")

    gender = fields.Char(string="Gender")
    qualification = fields.Char(string ="Qualification")
    hobby = fields.Char(String="Hobby")
    address = fields.Char(string="Adress")
    permanent_adress = fields.Char(string="Permanent Address")

    email = fields.Char(string ="Email")
    facebook = fields.Char(string="Facebook")
    phone = fields.Char(string="Phone")
    field_of_interest = fields.Char(string = "Field of Interest")
    working_experience = fields.Char(string="Working Experience")
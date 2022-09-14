from odoo import api, fields, models

class ResellerCardXlsx(models.AbstractModel):
    _name = 'report.rezzstore.report_resellercard_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    tgl = fields.Date.today()

    def generate_xlsx_report(self, workbook, data, reseller):
        bold = workbook.add_format({'bold' : True})
        format_1 = workbook.add_format({'bold' : True, 'align' : 'center', 'bg_color' : 'blue'})

        for obj in reseller:
            import base64
            import io

            sheet = workbook.add_worksheet(obj.name)
            row = 3
            col = 3
            sheet.set_column('D:D', 12)
            sheet.set_column('E:E', 13)

            row += 1
            sheet.merge_range(row, col, row, col + 1, 'RESELLER CARD', format_1)

            row += 1
            if obj.foto:
                foto = io.BytesIO(base64.b64decode(obj.foto))
                sheet.insert_image(row, col, "foto.png", {'image_data' : foto, 'x_scale' : 0.5, 'y_scale' : 0.5})

                row += 6
            sheet.write(row, col, 'Nama', bold)
            sheet.write(row, col + 1, obj.name)
            row += 1
            sheet.write(row, col, 'Alamat', bold)
            sheet.write(row, col + 1, obj.alamat)
            row += 1
            sheet.write(row, col, 'No. Handphone', bold)
            sheet.write(row, col + 1, obj.no_hp)
            row += 1
            sheet.write(row, col, 'E-Mail', bold)
            sheet.write(row, col + 1, obj.email)
            
            row += 2

            sheet.merge_range(row, col, row + 2, col + 1, 'RESELLER CARD', format_1)
# GCC Invoice Layout Module

Custom Odoo 18 invoice layout module for Tax Invoice generation with Arabic/English support.

## Installation

1. Place the `gcc_invoice_layout` folder in your Odoo addons directory.
2. Update Apps list in Odoo.
3. Search for and install "GCC Invoice Layout Customization".

## Features

- **Bilingual Support**: English and Arabic invoice headers
- **Custom Font**: Uses Cairo font for Arabic text
- **Tax Invoice Format**: Compliant with GCC tax requirements
- **QR Code Ready**: Structure supports QR code integration
- **Professional Layout**: Modern design with company branding

## Usage

After installation:

1. Go to Accounting > Invoices
2. Select an invoice
3. Print using "Tax Invoice" report

## Customization

- Modify `report/invoice_template.xml` to adjust layout
- Update colors in `static/src/css/invoice_report.css`
- Add company logo by modifying the header section

## Font Support

The module uses Google Fonts (Cairo) for Arabic text. Ensure your Odoo server has internet access or download the font locally.

## Support

For issues or customizations, contact your development team.
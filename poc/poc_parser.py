from lxml import html
import requests
import re


def well_details(api_number):
    url = "https://wwwapps.emnrd.nm.gov/OCD/OCDPermitting/Data/WellDetails.aspx"
    querystring = {"api": api_number}
    headers = {
        'accept': "*/*"
    }

    return requests.request("GET", url, headers=headers, params=querystring)

def parse_field(response, field_name):
    try:
        tree = html.fromstring(response.text)

        element = tree.cssselect(f'#{field_name}')[0]
        element_html = html.tostring(element, pretty_print=True).decode()

        # Use regex to extract data between tags
        match = re.search(r'>(.+?)<', element_html)
        if match:
            return ''.join([m.strip() for m in re.findall(r'>(.+?)<', element_html)])
        else:
            return None
    except IndexError:
        return None

response = well_details("30-045-35432")

lblOperator = parse_field(
    response, "ctl00_ctl00__main_main_ucGeneralWellInformation_lblOperator")
lblStatus = parse_field(
    response, "ctl00_ctl00__main_main_ucGeneralWellInformation_lblStatus")
lblWellType = parse_field(
    response, "ctl00_ctl00__main_main_ucGeneralWellInformation_lblWellType")
lblWorkType = parse_field(
    response, "ctl00_ctl00__main_main_ucGeneralWellInformation_lblWorkType")
lblDirectionalStatus = parse_field(
    response, "ctl00_ctl00__main_main_ucGeneralWellInformation_lblDirectionalStatus")
lblMultiLateral = parse_field(
    response, "ctl00_ctl00__main_main_ucGeneralWellInformation_lblMultiLateral")
lblMineralOwner = parse_field(
    response, "ctl00_ctl00__main_main_ucGeneralWellInformation_lblMineralOwner")
lblSurfaceOwner = parse_field(
    response, "ctl00_ctl00__main_main_ucGeneralWellInformation_lblSurfaceOwner")
lblLocation = parse_field(
    response, "ctl00_ctl00__main_main_ucGeneralWellInformation_Location_lblLocation")
lblText = parse_field(
    response, "ctl00_ctl00__main_main_ucGeneralWellInformation_Location_lblText")
lblLot = parse_field(
    response, "ctl00_ctl00__main_main_ucGeneralWellInformation_Location_lblLot")
lblFootageNSH = parse_field(
    response, "ctl00_ctl00__main_main_ucGeneralWellInformation_Location_lblFootageNSH")
lblFootageEW = parse_field(
    response, "ctl00_ctl00__main_main_ucGeneralWellInformation_Location_lblFootageEW")
lblCoordinates = parse_field(
    response, "ctl00_ctl00__main_main_ucGeneralWellInformation_Location_lblCoordinates")
lblGLElevation = parse_field(
    response, "ctl00_ctl00__main_main_ucGeneralWellInformation_lblGLElevation")
lblKBElevation = parse_field(
    response, "ctl00_ctl00__main_main_ucGeneralWellInformation_lblKBElevation")
lblDFElevation = parse_field(
    response, "ctl00_ctl00__main_main_ucGeneralWellInformation_lblDFElevation")
lblCompletions = parse_field(
    response, "ctl00_ctl00__main_main_ucGeneralWellInformation_lblCompletions")
lblPotashWaiver = parse_field(
    response, "ctl00_ctl00__main_main_ucGeneralWellInformation_lblPotashWaiver")
lblProposedFormation = parse_field(
    response, "ctl00_ctl00__main_main_ucGeneralWellInformation_lblProposedFormation")
lblProposedDepth = parse_field(
    response, "ctl00_ctl00__main_main_ucGeneralWellInformation_lblProposedDepth")
lblMeasuredVerticalDepth = parse_field(
    response, "ctl00_ctl00__main_main_ucGeneralWellInformation_lblMeasuredVerticalDepth")
lblTrueVerticalDepth = parse_field(
    response, "ctl00_ctl00__main_main_ucGeneralWellInformation_lblTrueVerticalDepth")
lblPlugbackMeasuredDpth = parse_field(
    response, "ctl00_ctl00__main_main_ucGeneralWellInformation_lblPlugbackMeasuredDpth")
lblApdInitialApprovalDate = parse_field(
    response, "ctl00_ctl00__main_main_ucGeneralWellInformation_lblApdInitialApprovalDate")
lblApdEffectiveDate = parse_field(
    response, "ctl00_ctl00__main_main_ucGeneralWellInformation_lblApdEffectiveDate")
lblApdCancellationDate = parse_field(
    response, "ctl00_ctl00__main_main_ucGeneralWellInformation_lblApdCancellationDate")
lblApdExtensionApprovalEffectiveDate = parse_field(
    response, "ctl00_ctl00__main_main_ucGeneralWellInformation_lblApdExtensionApprovalEffectiveDate")
lblSpudDate = parse_field(
    response, "ctl00_ctl00__main_main_ucGeneralWellInformation_lblSpudDate")
lblTADate = parse_field(
    response, "ctl00_ctl00__main_main_ucGeneralWellInformation_lblTADate")
lblShutInWaitingForPipelineDate = parse_field(
    response, "ctl00_ctl00__main_main_ucGeneralWellInformation_lblShutInWaitingForPipelineDate")
lblPluggedAbandonedDateIntent = parse_field(
    response, "ctl00_ctl00__main_main_ucGeneralWellInformation_lblPluggedAbandonedDateIntent")
lblPluggedDate = parse_field(
    response, "ctl00_ctl00__main_main_ucGeneralWellInformation_lblPluggedDate")
lblSiteReleaseDate = parse_field(
    response, "ctl00_ctl00__main_main_ucGeneralWellInformation_lblSiteReleaseDate")
lblLastInspectionDate = parse_field(
    response, "ctl00_ctl00__main_main_ucGeneralWellInformation_lblLastInspectionDate")
lblLastInspectionDateLable = parse_field(
    response, "ctl00_ctl00__main_main_ucGeneralWellInformation_lblLastInspectionDateLable")
lblApdExpirationDate = parse_field(
    response, "ctl00_ctl00__main_main_ucGeneralWellInformation_lblApdExpirationDate")
lblGasCapturePlanDate = parse_field(
    response, "ctl00_ctl00__main_main_ucGeneralWellInformation_lblGasCapturePlanDate")
lblTAExpirationDate = parse_field(
    response, "ctl00_ctl00__main_main_ucGeneralWellInformation_lblTAExpirationDate")
lblPluggedNotReleasedExpirationDate = parse_field(
    response, "ctl00_ctl00__main_main_ucGeneralWellInformation_lblPluggedNotReleasedExpirationDate")
lblLastMitDate = parse_field(
    response, "ctl00_ctl00__main_main_ucGeneralWellInformation_lblLastMitDate")

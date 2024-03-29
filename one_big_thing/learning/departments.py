# List of departments/organisations
# Let 10DS (Cailin) know if these change as it has an impact on their analysis

from . import utils

department_tuples = (
    ("acas", "The Advisory, Conciliation and Arbitration Service (Acas)"),
    ("active-travel-england", "Active Travel England (ATE)"),
    ("advisory-committee-on-releases-to-the-environment", "Advisory Committee on Releases to the Environment (ACRE)"),
    ("agriculture-and-horticulture-development-board", "Agriculture and Horticulture Development Board (AHDB)"),
    ("animal-and-plant-health-agency", "Animal and Plant Health Agency (APHA)"),
    ("attorney-generals-office", "Attorney General's Office (AGO)"),
    ("board-of-trustees-of-the-royal-botanic-gardens-kew", "Board of Trustees of the Royal Botanic Gardens Kew"),
    ("border-force", "Border Force"),
    ("british-wool", "British Wool"),
    ("broads-authority", "Broads Authority"),
    ("building-digital-uk", "Building Digital UK (BDUK)"),
    ("cabinet-office", "Cabinet Office"),
    ("central-civil-service-fast-stream", "Central Civil Service Fast Stream"),
    (
        "centre-for-environment-fisheries-and-aquaculture-science",
        "Centre for Environment, Fisheries and Aquaculture Science (Cefas)",
    ),
    ("charity-commission", "The Charity Commission (Charity Commission)"),
    ("companies-house", "Companies House  (Companies House)"),
    ("competition-and-markets-authority", "Competition and Markets Authority (CMA)"),
    ("construction-industry-training-board", "Construction Industry Training Board (CITB)"),
    ("consumer-council-for-water", "Consumer Council for Water (CCW)"),
    ("covent-garden-market-authority", "Covent Garden Market Authority (CGMA)"),
    ("criminal-injuries-compensation-appeals-panel", "Criminal Injuries Compensation Appeals Panel"),
    ("crown-commercial-service", "Crown Commercial Service (CCS)"),
    ("crown-prosecution-service", "Crown Prosecution Service (CPS)"),
    ("dartmoor-national-park-authority", "Dartmoor National Park Authority (DNPA)"),
    ("defence-electronics-and-components-agency", "Defence Electronics and Components Agency (DECA)"),
    ("defence-equipment-and-support", "Defence Equipment and Support (DE&S)"),
    ("defence-nuclear-organisation", "Defence Nuclear Organisation (DNO)"),
    ("defence-science-and-technology-laboratory", "Defence Science and Technology Laboratory (Dstl)"),
    ("science-advisory-council", "Defra's Science Advisory Council (SAC)"),
    ("department-for-business-and-trade", "Department for Business and Trade (DBT)"),
    ("department-for-culture-media-and-sport", "Department for Culture, Media and Sport (DCMS)"),
    ("department-for-education", "Department for Education (DfE)"),
    ("department-for-energy-security-and-net-zero", "Department for Energy Security and Net Zero (DESNZ)"),
    ("department-for-environment-food-rural-affairs", "Department for Environment, Food & Rural Affairs (Defra)"),
    (
        "department-for-levelling-up-housing-and-communities",
        "Department for Levelling Up, Housing and Communities  (DLUHC)",
    ),
    ("department-for-science-innovation-and-technology", "Department for Science, Innovation and Technology (DSIT)"),
    ("department-for-transport", "Department for Transport (DfT)"),
    ("department-of-health-and-social-care", "Department of Health and Social Care (DHSC)"),
    ("disclosure-and-barring-service", "Disclosure and Barring Service (DBS)"),
    ("driver-and-vehicle-licensing-agency", "Driver and Vehicle Licensing Agency (DVLA)"),
    ("driver-and-vehicle-standards-agency", "Driver and Vehicle Standards Agency (DVSA)"),
    ("dwp-central-analysis-and-science", "DWP Central Analysis and Science"),
    ("dwp-change-group", "DWP Change Group"),
    ("dwp-communications", "DWP Communications"),
    ("dwp-corporate-transformantion", "DWP Corporate Transformation"),
    ("dwp-digital-it", "DWP Digital IT"),
    ("dwp-finance-group", "DWP Finance Group"),
    ("dwp-ops-cmg", "DWP Operations - Service Excellence, Child Maintenance Group"),
    ("dwp-ops-cfed", "DWP Operations - Service Excellence, Counter Fraud, Error and Debt"),
    ("dwp-ops-ce", "DWP Operations - Service Excellence, Customer Experience"),
    ("dwp-ops-drs", "DWP Operations - Service Excellence, Dispute Resolution Service"),
    ("dwp-ops-rs", "DWP Operations - Service Excellence, Retirement Services"),
    ("dwp-ops-sm", "DWP Operations - Service Excellence, Service Modernisation"),
    ("dwp-ops-spd", "DWP Operations - Service Excellence, Service Planning and Delivery"),
    (
        "dwp-ops-dsdmwa",
        "DWP Operations - Work and Health, Disability Services Decision Making and Working Age Directorate",
    ),
    ("dwp-ops-uco", "DWP Operations - Work and Health, Universal Credit Operations"),
    ("dwp-people-and-capability", "DWP People and Capability"),
    ("dwp-policy-team", "DWP Policy Team"),
    ("dwp-private-office", "DWP Private Office"),
    ("dwp-strategy-directorate", "DWP Strategy Directorate"),
    ("dwp-other", "DWP - Other"),
    ("education-and-skills-funding-agency", "Education and Skills Funding Agency (ESFA)"),
    ("engineering-construction-industry-training-board", "Engineering Construction Industry Training Board (ECITB)"),
    ("environment-agency", "Environment Agency (EA)"),
    ("the-equality-hub", "Equality Hub"),
    ("estyn", "Estyn"),
    ("exmoor-national-park-authority", "Exmoor National Park Authority (Exmoor)"),
    ("fcdo-services", "FCDO Services"),
    ("flood-re", "Flood Re"),
    ("food-standards-agency", "Food Standards Agency (FSA)"),
    ("foreign-commonwealth-development-office", "Foreign, Commonwealth & Development Office (FCDO)"),
    ("forestry-commission", "Forestry Commission (Forestry Commission)"),
    ("government-actuarys-department", "Government Actuary's Department (GAD)"),
    ("government-commercial-organisation", "Government Commercial Organisation"),
    ("government-equalities-office", "Government Equalities Office (GEO)"),
    ("government-internal-audit-agency", "Government Internal Audit Agency (GIAA)"),
    ("government-legal-department", "Government Legal Department (GLD)"),
    ("government-property-agency", "Government Property Agency (GPA)"),
    ("health-and-safety-executive", "Health and Safety Executive (HSE)"),
    ("hm-courts-and-tribunals-service", "HM Courts & Tribunals Service (HMCTS)"),
    ("hm-inspectorate-of-prisons", "HM Inspectorate of Prisons"),
    ("hm-inspectorate-of-probation", "HM Inspectorate of Probation"),
    ("land-registry", "HM Land Registry (HM Land Registry)"),
    ("hm-prison-and-probation-service", "HM Prison and Probation Service (HMPPS)"),
    ("hm-revenue-customs", "HM Revenue & Customs (HMRC)"),
    ("hm-treasury", "HM Treasury (HMT)"),
    ("home-office", "Home Office (Home Office)"),
    ("hm-passport-office", "HM Passport Office (HM Passport Office)"),
    ("identity-and-passport-service", "Identity and Passport Service"),
    ("immigration-enforcement", "Immigration Enforcement"),
    ("independent-agricultural-appeals-panel", "Independent Agricultural Appeals Panel (IAAP)"),
    (
        "independent-monitoring-boards-of-prisons-immigration-removal-centres-and-short-term-holding-rooms",
        "Independent Monitoring Boards (IMB)",
    ),
    ("infrastructure-and-projects-authority", "Infrastructure and Projects Authority (IPA)"),
    ("institute-for-apprenticeships-and-technical-education", "Institute for Apprenticeships and Technical Education"),
    ("intellectual-property-office", "Intellectual Property Office (IPO)"),
    ("joint-nature-conservation-committee", "Joint Nature Conservation Committee (JNCC)"),
    ("judicial-appointments-and-conduct-ombudsman", "Judicial Appointments and Conduct Ombudsman (JACO)"),
    ("judicial-office", "Judicial Office (JO)"),
    ("lake-district-national-park-authority", "Lake District National Park Authority (LDNP)"),
    ("law-commission", "Law Commission"),
    ("legal-aid-agency", "Legal Aid Agency (LAA)"),
    ("located", "LocatED"),
    ("marine-management-organisation", "Marine Management Organisation (MMO)"),
    ("maritime-and-coastguard-agency", "Maritime and Coastguard Agency (MCA)"),
    (
        "medicines-and-healthcare-products-regulatory-agency",
        "Medicines and Healthcare products Regulatory Agency (MHRA)",
    ),
    ("met-office", "Met Office"),
    ("ministry-of-defence-civilian", "Ministry of Defence (MOD) - Civilian Staff"),
    ("ministry-of-defence-military", "Ministry of Defence (MOD) - Military Staff"),
    ("ministry-of-justice", "Ministry of Justice (MOJ)"),
    ("single-financial-guidance-body", "Money and Pensions Service (MaPS)"),
    ("national-crime-agency", "National Crime Agency (NCA)"),
    ("national-forest-company", "National Forest Company (NFC)"),
    ("national-infrastructure-commission", "National Infrastructure Commission"),
    ("natural-england", "Natural England (Natural England)"),
    ("new-forest-national-park-authority", "New Forest National Park Authority (NFNPA)"),
    ("north-york-moors-national-park", "North York Moors National Park Authority (NYMNP)"),
    ("northern-ireland-executive", "Northern Ireland Executive "),
    ("northern-ireland-office", "Northern Ireland Office (NIO)"),
    ("northumberland-national-park-authority", "Northumberland National Park Authority"),
    ("ns-i", "NS&I (NS&I)"),
    ("oak-national-academy", "Oak National Academy"),
    ("office-for-environmental-protection", "Office for Environmental Protection (OEP)"),
    ("office-for-national-statistics", "Office for National Statistics (ONS)"),
    ("ofsted", "Office for Standards in Education, Children's Services and Skills (Ofsted)"),
    ("office-for-students", "Office for Students (OfS)"),
    ("ofgem", "Office of Gas and Electricity Markets (Ofgem)"),
    ("ofqual", "Office of Qualifications and Examinations Regulation (Ofqual)"),
    ("office-of-rail-and-road", "Office of Rail and Road (ORR)"),
    ("office-of-the-advocate-general-for-scotland", "Office of the Advocate General for Scotland (OAG)"),
    ("office-of-the-children-s-commissioner", "Office of the Children's Commissioner"),
    ("the-office-of-the-leader-of-the-house-of-commons", "Office of the Leader of the House of Commons (OLHC)"),
    ("office-of-the-leader-of-the-house-of-lords", "Office of the Leader of the House of Lords (OLHL)"),
    ("office-of-the-public-guardian", "Office of the Public Guardian (OPG)"),
    ("office-of-the-secretary-of-state-for-scotland", "Office of the Secretary of State for Scotland"),
    (
        "office-of-the-secretary-of-state-for-wales",
        "Office of the Secretary of State for Wales (UK Government in Wales)",
    ),
    ("official-solicitor-and-public-trustee", "Official Solicitor and Public Trustee (OSPT)"),
    ("peak-district-national-park", "Peak District National Park Authority (PDNP)"),
    ("planning-inspectorate", "Planning Inspectorate (The Planning Inspectorate)"),
    ("plant-varieties-and-seeds-tribunal", "Plant Varieties and Seeds Tribunal (PVST)"),
    ("prime-ministers-office-10-downing-street", "Prime Minister's Office, 10 Downing Street (Number 10)"),
    ("prisons-and-probation-ombudsman", "Prisons and Probation Ombudsman (PPO)"),
    ("queen-elizabeth-ii-conference-centre", "Queen Elizabeth II Conference Centre (QEIICC)"),
    ("royal-fleet-auxiliary", "Royal Fleet Auxiliary"),
    ("rural-payments-agency", "Rural Payments Agency (RPA)"),
    ("the-scottish-government", "The Scottish Government (The Scottish Government)"),
    ("seafish", "Seafish (Seafish)"),
    ("the-sentencing-council-for-england-and-wales", "Sentencing Council for England and Wales (SC)"),
    ("serious-fraud-office", "Serious Fraud Office (SFO)"),
    ("social-work-england", "Social Work England"),
    ("south-downs-national-park-authority", "South Downs National Park Authority (SDNP)"),
    ("standards-and-testing-agency", "Standards and Testing Agency (STA)"),
    ("student-loans-company", "Student Loans Company (SLC)"),
    ("submarine-delivery-agency", "Submarine Delivery Agency (SDA)"),
    ("supreme-court-of-the-united-kingdom", "Supreme Court of the United Kingdom (SCUK)"),
    ("teaching-regulation-agency", "Teaching Regulation Agency (TRA)"),
    ("insolvency-service", "The Insolvency Service"),
    ("the-national-archives", "The National Archives"),
    ("the-water-services-regulation-authority", "The Water Services Regulation Authority (Ofwat)"),
    ("uk-debt-management-office", "UK Debt Management Office (DMO)"),
    ("uk-export-finance", "UK Export Finance (UKEF)"),
    ("uk-health-security-agency", "UK Health Security Agency (UKHSA)"),
    ("uk-hydrographic-office", "UK Hydrographic Office (UKHO)"),
    ("uk-space-agency", "UK Space Agency"),
    ("uk-statistics-authority", "UK Statistics Authority (Statistics)"),
    ("valuation-office-agency", "Valuation Office Agency (VOA)"),
    ("vehicle-certification-agency", "Vehicle Certification Agency (VCA)"),
    ("veterinary-medicines-directorate", "Veterinary Medicines Directorate (VMD)"),
    ("veterinary-products-committee", "Veterinary Products Committee (VPC)"),
    ("victims-commissioner", "Victims' Commissioner"),
    ("welsh-government", "Welsh Government"),
    ("welsh-revenue-authority", "Welsh Revenue Authority"),
    ("wilton-park", "Wilton Park (Wilton Park)"),
    ("yorkshire-dales-national-park-authority", "Yorkshire Dales National Park Authority (YDNP)"),
    ("other", "Other"),
    ("other-civil-servant", "Other - Civil Servant"),
    ("other-public-servant", "Other - Public Servant"),
)

Department = utils.Choices("Department", department_tuples)

from datetime import date

import boundaries

boundaries.register('Ontario electoral districts',
    domain='Ontario',
    last_updated=date(2011, 6, 2),
    name_func=boundaries.clean_attr('ENGLISH_NA'),
    id_func=boundaries.attr('ED_ID'),
    authority='Government of Ontario',
    source_url='http://www.elections.on.ca/en-CA/Tools/ElectoralDistricts/Shapefile.htm',
    licence_url='http://www.elections.on.ca/en-CA/Tools/ElectoralDistricts/LimitedUseDataProductLicenceAgreement.htm',
    data_url='http://www.elections.on.ca/NR/rdonlyres/C34F1D43-8086-46EC-A013-C0EF42A8CC09/0/EO_107ED_2011_06_02.zip',
    encoding='iso-8859-1',
)

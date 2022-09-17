def VotersPerConstituency(voters):
    vpc = voters.COUNTY_NAME.value_counts().reset_index()
    vpc.rename(columns={'index':'County', 'COUNTY_NAME':'Number of Constituencies'}, inplace=True)
    return vpc

def ConstituencyPerVotersCount(voters):
    cnv = voters.groupby('CONSTITUENCY_NAME')[['VOTERS']].sum().reset_index()
    return cnv

def ConstituenciesPerPollingStations(voters):
    vpx = voters.groupby(['COUNTY_NAME','CONSTITUENCY_NAME'])['NO. OF POLLING STATIONS'].sum().reset_index()
    return vpx
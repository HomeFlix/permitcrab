import datetime
import jinja2
import requests
import sys
from bs4 import BeautifulSoup
from http.client import HTTPConnection #py3
# print statements from `http.client.HTTPConnection` to console/stdout
# HTTPConnection.debuglevel = 1

print("                   __       __    ")
print("                  / <`     '> \   ")
print("                 (  / @   @ \  )  ")
print("                  \(_ _\_/_ _)/   ")
print("                (\ `-/     \-' /) ")
print("                 \"===\     /===\"")
print("                  .==')___(`==.   ")
print("                 ' .='     `=.    ")
print("")
print("    Welcome to Permit Crab .........")
print("    Crawling Raleigh's Permit Portal")
print("    So that you don't have to ......")
print("")
print("    Target Locked: " + sys.argv[1])

if len(sys.argv) == 1:
    print('Usage: python3 ' + sys.argv[0] + ' <Target Wake County Address with Street Number, Street Name and Abbreviated Descriptor> Example: python3 generate.py \"5001 Coronado Dr\"')
    sys.exit()
else:
    targetaddress = sys.argv[1]

def flatten(xs):
    for x in xs:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            yield from flatten(x)
        else:
            yield x

def makeReadableDates(list1):
    readable_list = []
    for x in list1:
        readable_list.append(x.strftime("%B") + " " + x.strftime("%Y"))
    return readable_list

def uniqueYearMonth(l):
    s = set(e[0] for e in l)
    return sorted(list(s),reverse=True)

# function to get unique values
def unique(list1):
    # initialize a null list
    unique_list = []
    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    # print list
    #for x in unique_list:
        #list(filter(None, unique_list))
        #print(x)
    return x

permit_detail_url = 'https://raleighnc-energovpub.tylerhost.net/apps/selfservice/api/energov/permits/permitdetail'

url = 'https://raleighnc-energovpub.tylerhost.net/apps/selfservice/api/energov/search/search'
headers = {'Content-type': 'application/json;charset=UTF-8',
           'tenantId': '1',
           'tenantName': 'RaleighNCProd',
           'Tyler-Tenant-Culture': 'en-US',
           'Tyler-TenantUrl': 'RaleighNCProd',
           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'}
myobj = '''{
  "Keyword": "''' + targetaddress + '''",
  "ExactMatch": true,
  "SearchModule": 1,
  "FilterModule": 1,
  "SearchMainAddress": false,
  "PlanCriteria": {
    "PlanNumber": null,
    "PlanTypeId": null,
    "PlanWorkclassId": null,
    "PlanStatusId": null,
    "ProjectName": null,
    "ApplyDateFrom": null,
    "ApplyDateTo": null,
    "ExpireDateFrom": null,
    "ExpireDateTo": null,
    "CompleteDateFrom": null,
    "CompleteDateTo": null,
    "Address": null,
    "Description": null,
    "SearchMainAddress": false,
    "ContactId": null,
    "ParcelNumber": null,
    "TypeId": null,
    "WorkClassIds": null,
    "ExcludeCases": null,
    "EnableDescriptionSearch": false,
    "PageNumber": 0,
    "PageSize": 0,
    "SortBy": "relevance",
    "SortAscending": false
  },
  "PermitCriteria": {
    "PermitNumber": null,
    "PermitTypeId": null,
    "PermitWorkclassId": null,
    "PermitStatusId": null,
    "ProjectName": null,
    "IssueDateFrom": null,
    "IssueDateTo": null,
    "Address": null,
    "Description": null,
    "ExpireDateFrom": null,
    "ExpireDateTo": null,
    "FinalDateFrom": null,
    "FinalDateTo": null,
    "ApplyDateFrom": null,
    "ApplyDateTo": null,
    "SearchMainAddress": false,
    "ContactId": null,
    "TypeId": null,
    "WorkClassIds": null,
    "ParcelNumber": null,
    "ExcludeCases": null,
    "EnableDescriptionSearch": false,
    "PageNumber": 0,
    "PageSize": 0,
    "SortBy": null,
    "SortAscending": false
  },
  "InspectionCriteria": {
    "Keyword": null,
    "ExactMatch": false,
    "Complete": null,
    "InspectionNumber": null,
    "InspectionTypeId": null,
    "InspectionStatusId": null,
    "RequestDateFrom": null,
    "RequestDateTo": null,
    "ScheduleDateFrom": null,
    "ScheduleDateTo": null,
    "Address": null,
    "SearchMainAddress": false,
    "ContactId": null,
    "TypeId": [
      
    ],
    "WorkClassIds": [
      
    ],
    "ParcelNumber": null,
    "DisplayCodeInspections": false,
    "ExcludeCases": [
      
    ],
    "ExcludeFilterModules": [
      
    ],
    "HiddenInspectionTypeIDs": null,
    "PageNumber": 0,
    "PageSize": 0,
    "SortBy": null,
    "SortAscending": false
  },
  "CodeCaseCriteria": {
    "CodeCaseNumber": null,
    "CodeCaseTypeId": null,
    "CodeCaseStatusId": null,
    "ProjectName": null,
    "OpenedDateFrom": null,
    "OpenedDateTo": null,
    "ClosedDateFrom": null,
    "ClosedDateTo": null,
    "Address": null,
    "ParcelNumber": null,
    "Description": null,
    "SearchMainAddress": false,
    "RequestId": null,
    "ExcludeCases": null,
    "ContactId": null,
    "EnableDescriptionSearch": false,
    "PageNumber": 0,
    "PageSize": 0,
    "SortBy": null,
    "SortAscending": false
  },
  "RequestCriteria": {
    "RequestNumber": null,
    "RequestTypeId": null,
    "RequestStatusId": null,
    "ProjectName": null,
    "EnteredDateFrom": null,
    "EnteredDateTo": null,
    "DeadlineDateFrom": null,
    "DeadlineDateTo": null,
    "CompleteDateFrom": null,
    "CompleteDateTo": null,
    "Address": null,
    "ParcelNumber": null,
    "SearchMainAddress": false,
    "PageNumber": 0,
    "PageSize": 0,
    "SortBy": null,
    "SortAscending": false
  },
  "BusinessLicenseCriteria": {
    "LicenseNumber": null,
    "LicenseTypeId": null,
    "LicenseClassId": null,
    "LicenseStatusId": null,
    "BusinessStatusId": null,
    "LicenseYear": null,
    "ApplicationDateFrom": null,
    "ApplicationDateTo": null,
    "IssueDateFrom": null,
    "IssueDateTo": null,
    "ExpirationDateFrom": null,
    "ExpirationDateTo": null,
    "SearchMainAddress": false,
    "CompanyTypeId": null,
    "CompanyName": null,
    "BusinessTypeId": null,
    "Description": null,
    "CompanyOpenedDateFrom": null,
    "CompanyOpenedDateTo": null,
    "CompanyClosedDateFrom": null,
    "CompanyClosedDateTo": null,
    "LastAuditDateFrom": null,
    "LastAuditDateTo": null,
    "ParcelNumber": null,
    "Address": null,
    "TaxID": null,
    "DBA": null,
    "ExcludeCases": null,
    "TypeId": null,
    "WorkClassIds": null,
    "ContactId": null,
    "PageNumber": 0,
    "PageSize": 0,
    "SortBy": null,
    "SortAscending": false
  },
  "ProfessionalLicenseCriteria": {
    "LicenseNumber": null,
    "HolderFirstName": null,
    "HolderMiddleName": null,
    "HolderLastName": null,
    "HolderCompanyName": null,
    "LicenseTypeId": null,
    "LicenseClassId": null,
    "LicenseStatusId": null,
    "IssueDateFrom": null,
    "IssueDateTo": null,
    "ExpirationDateFrom": null,
    "ExpirationDateTo": null,
    "ApplicationDateFrom": null,
    "ApplicationDateTo": null,
    "Address": null,
    "MainParcel": null,
    "SearchMainAddress": false,
    "ExcludeCases": null,
    "TypeId": null,
    "WorkClassIds": null,
    "ContactId": null,
    "PageNumber": 0,
    "PageSize": 0,
    "SortBy": null,
    "SortAscending": false
  },
  "LicenseCriteria": {
    "LicenseNumber": null,
    "LicenseTypeId": null,
    "LicenseClassId": null,
    "LicenseStatusId": null,
    "BusinessStatusId": null,
    "ApplicationDateFrom": null,
    "ApplicationDateTo": null,
    "IssueDateFrom": null,
    "IssueDateTo": null,
    "ExpirationDateFrom": null,
    "ExpirationDateTo": null,
    "SearchMainAddress": false,
    "CompanyTypeId": null,
    "CompanyName": null,
    "BusinessTypeId": null,
    "Description": null,
    "CompanyOpenedDateFrom": null,
    "CompanyOpenedDateTo": null,
    "CompanyClosedDateFrom": null,
    "CompanyClosedDateTo": null,
    "LastAuditDateFrom": null,
    "LastAuditDateTo": null,
    "ParcelNumber": null,
    "Address": null,
    "TaxID": null,
    "DBA": null,
    "ExcludeCases": null,
    "TypeId": null,
    "WorkClassIds": null,
    "ContactId": null,
    "HolderFirstName": null,
    "HolderMiddleName": null,
    "HolderLastName": null,
    "MainParcel": null,
    "EnableDescriptionSearchForBLicense": false,
    "EnableDescriptionSearchForPLicense": false,
    "PageNumber": 0,
    "PageSize": 0,
    "SortBy": null,
    "SortAscending": false
  },
  "ProjectCriteria": {
    "ProjectNumber": null,
    "ProjectName": null,
    "Address": null,
    "ParcelNumber": null,
    "StartDateFrom": null,
    "StartDateTo": null,
    "ExpectedEndDateFrom": null,
    "ExpectedEndDateTo": null,
    "CompleteDateFrom": null,
    "CompleteDateTo": null,
    "Description": null,
    "SearchMainAddress": false,
    "ContactId": null,
    "TypeId": null,
    "ExcludeCases": null,
    "EnableDescriptionSearch": false,
    "PageNumber": 0,
    "PageSize": 0,
    "SortBy": null,
    "SortAscending": false
  },
  "PlanSortList": [
    {
      "Key": "relevance",
      "Value": "Relevance"
    },
    {
      "Key": "PlanNumber.keyword",
      "Value": "Plan Number"
    },
    {
      "Key": "ProjectName.keyword",
      "Value": "Project"
    },
    {
      "Key": "MainAddress",
      "Value": "Address"
    },
    {
      "Key": "ApplyDate",
      "Value": "Apply Date"
    }
  ],
  "PermitSortList": [
    {
      "Key": "relevance",
      "Value": "Relevance"
    },
    {
      "Key": "PermitNumber.keyword",
      "Value": "Permit Number"
    },
    {
      "Key": "ProjectName.keyword",
      "Value": "Project"
    },
    {
      "Key": "MainAddress",
      "Value": "Address"
    },
    {
      "Key": "IssueDate",
      "Value": "Issued Date"
    },
    {
      "Key": "FinalDate",
      "Value": "Finalized Date"
    }
  ],
  "InspectionSortList": [
    {
      "Key": "relevance",
      "Value": "Relevance"
    },
    {
      "Key": "InspectionNumber.keyword",
      "Value": "Inspection Number"
    },
    {
      "Key": "MainAddress",
      "Value": "Address"
    },
    {
      "Key": "ScheduledDate",
      "Value": "Schedule Date"
    },
    {
      "Key": "RequestDate",
      "Value": "Request Date"
    }
  ],
  "CodeCaseSortList": [
    {
      "Key": "relevance",
      "Value": "Relevance"
    },
    {
      "Key": "CaseNumber.keyword",
      "Value": "Code Case Number"
    },
    {
      "Key": "ProjectName.keyword",
      "Value": "Project"
    },
    {
      "Key": "MainAddress",
      "Value": "Address"
    },
    {
      "Key": "OpenedDate",
      "Value": "Opened Date"
    },
    {
      "Key": "ClosedDate",
      "Value": "Closed Date"
    }
  ],
  "RequestSortList": [
    {
      "Key": "relevance",
      "Value": "Relevance"
    },
    {
      "Key": "RequestNumber.keyword",
      "Value": "Request Number"
    },
    {
      "Key": "ProjectName.keyword",
      "Value": "Project Name"
    },
    {
      "Key": "MainAddress",
      "Value": "Address"
    },
    {
      "Key": "EnteredDate",
      "Value": "Date Entered"
    },
    {
      "Key": "CompleteDate",
      "Value": "Completion Date"
    }
  ],
  "LicenseSortList": [
    {
      "Key": "relevance",
      "Value": "Relevance"
    },
    {
      "Key": "LicenseNumber.keyword",
      "Value": "License Number"
    },
    {
      "Key": "CompanyName.keyword",
      "Value": "Company Name"
    },
    {
      "Key": "AppliedDate",
      "Value": "Applied Date"
    },
    {
      "Key": "MainAddress",
      "Value": "Address"
    }
  ],
  "ProjectSortList": [
    {
      "Key": "relevance",
      "Value": "Relevance"
    },
    {
      "Key": "ProjectNumber.keyword",
      "Value": "Project Number"
    },
    {
      "Key": "ProjectName.keyword",
      "Value": "Project Name"
    },
    {
      "Key": "StartDate",
      "Value": "Start Date"
    },
    {
      "Key": "CompleteDate",
      "Value": "Completed Date"
    },
    {
      "Key": "ExpectedEndDate",
      "Value": "Expected End Date"
    },
    {
      "Key": "MainAddress",
      "Value": "Address"
    }
  ],
  "ExcludeCases": null,
  "SortOrderList": [
    {
      "Key": true,
      "Value": "Ascending"
    },
    {
      "Key": false,
      "Value": "Descending"
    }
  ],
  "HiddenInspectionTypeIDs": null,
  "PageNumber": 1,
  "PageSize": 100,
  "SortBy": "relevance",
  "SortAscending": true
}'''

mycases = []
caseDates = []
yearMonths = []
permitScrape = requests.post(url, headers=headers, data = myobj)
permitJSON = permitScrape.json()
for cases in permitJSON["Result"]["EntityResults"]:
  if (cases["ScheduleDate"]) is not None:
    mycases.append([cases["CaseNumber"],datetime.datetime.strptime(cases["ScheduleDate"][:7], "%Y-%m").strftime("%B") + " " + datetime.datetime.strptime(cases["ScheduleDate"][:7], "%Y-%m").strftime("%Y"),datetime.datetime.strptime(cases["ScheduleDate"][:10], "%Y-%m-%d").strftime("%m/%d/%Y"),cases["CaseId"],cases["CaseType"],cases["CaseStatus"],cases["Description"]])
    caseDates.append((datetime.datetime.strptime(cases["ScheduleDate"][:7], "%Y-%m"),"ScheduleDate"))
    #caseDates.append((datetime.datetime.strptime(cases["ScheduleDate"][:10], "%Y-%m-%d").strftime("%b") + " " + datetime.datetime.strptime(cases["ScheduleDate"][:10], "%Y-%m-%d").strftime("%Y"),"ScheduleDate"))
    #print(datetime.datetime.strptime(cases["ScheduleDate"][:10], "%Y-%m-%d").strftime("%Y") + " - ScheduleDate")
  elif (cases["ApplyDate"]) is not None:
    mycases.append((cases["CaseNumber"],datetime.datetime.strptime(cases["ApplyDate"][:7], "%Y-%m").strftime("%B") + " " + datetime.datetime.strptime(cases["ApplyDate"][:7], "%Y-%m").strftime("%Y"),datetime.datetime.strptime(cases["ApplyDate"][:10], "%Y-%m-%d").strftime("%m/%d/%Y"),cases["CaseId"],cases["CaseType"],cases["CaseStatus"],cases["Description"]))
    caseDates.append((datetime.datetime.strptime(cases["ApplyDate"][:7], "%Y-%m"),"ApplyDate"))
    #caseDates.append((datetime.datetime.strptime(cases["ApplyDate"][:10], "%Y-%m-%d").strftime("%b") + " " + datetime.datetime.strptime(cases["ApplyDate"][:10], "%Y-%m-%d").strftime("%Y"),"ApplyDate"))
    #print("foo: " + datetime.datetime.strptime(cases["ApplyDate"][:10], "%Y-%m-%d").strftime("%Y"))
  else:
    mycases.append((cases["CaseNumber"],datetime.datetime.strptime("2000-01","%Y-%m").strftime("%B") + " " + datetime.datetime.strptime("2000-01", "%Y-%m").strftime("%Y"),datetime.datetime.strptime("2000-01-01", "%Y-%m-%d").strftime("%m/%d/%Y"),cases["CaseId"],cases["CaseType"],cases["CaseStatus"],cases["Description"]))
    caseDates.append((datetime.datetime.strptime("2000-01", "%Y-%m"),"DefaultDate"))

#2022-04-09T21:53:56.512357Z
#2020-07-28T15:27:51.6266667Z
entries = []
caselist = []
monthYear = makeReadableDates(uniqueYearMonth(caseDates))
for entry in monthYear:
  entries.append(list(filter(lambda c: c[1]==entry, mycases)))

for sublist in entries:
  for myentry in sublist:
    caselist.append(list(myentry))
caselist = sorted(caselist, key = lambda x: datetime.datetime.strptime(x[2],'%m/%d/%Y'),reverse=True)
outputfile = targetaddress.replace(" ", "_") + ".html"
subs = jinja2.Environment(
              loader=jinja2.FileSystemLoader('./')
              ).get_template('template.html').render(targetaddress=targetaddress,monthYear=monthYear,caselist=caselist)

tree = BeautifulSoup(subs,features="lxml")
good_html = tree.prettify()
# lets write the substitution to a file
with open(outputfile,'w') as f: f.write(good_html)

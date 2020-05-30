#!/usr/bin/env python
# coding: utf-8

# In[1]:


import jsonld


# # Issue 1

# ### KeyError: 'http://schema.org/item' #96 
# ### Link: https://github.com/digitalbazaar/pyld/issues/96

# In[2]:


x = jsonld.frame(
  {
    "@context": "http://schema.org",
    "@graph": [
      {
        "@type": "BreadcrumbList",
        "itemListElement": [
          {
            "@type": "ListItem",
            "item": {
              "@id": "https://example.com/",
              "@type": "WebPage",
              "url": "https://example.com/"
            }
          }
        ]
      }
    ]
  },
  {}
)


# In[3]:


print(x)


# # Issue 2

# ### JSON Literals not supported via @json KEYWORD #100
# ### Link : https://github.com/digitalbazaar/pyld/issues/100

# In[4]:



##Basic test case 1: 

document1 = jsonld.expand(
{
    "@context": {
      "@version": 1.1,
      "e": {"@id": "http://example.com/vocab/json", "@type": "@json"}
    },
    "e": [ 1,2,3,4 ]
  }
)

##Basic test case 2:

document2 = jsonld.expand(
{
    "@context": {
      "@version": 1.1,
      "e": {"@id": "http://example.com/vocab/json", "@type": "@json"}
    },
    "e": [ 1,2,3,4 ]
  }
)


# In[5]:



##Advanced Test Case original for issue 2 (1)
document3 = jsonld.expand( {
  "@context": {
    "@version": 1.1,
    "e": {"@id": "http://example.com/vocab/json", "@type": "@json"}
  },
  "e": {
    "json value": 56.0,
    "integrated_json":
    {
      "d": True,
      "10": None,
      "1": {"sweetchecker ": [1,2,3,4 ]}
    }
  }
})

##Advanced Test Case modified for issue 2 (2)
document4 = jsonld.expand( {
  "@context": {
    "@version": 1.1,
    "e": {"@id": "http://example.com/vocab/json", "@type": "@json"}
  },
  "e": [
    56.0,
    {
      "d": True,
      "10": None,
      "1": {"sweetchecker ": [1,2,3,4 ]}
    }
  ]
})


# In[6]:


print("Easy test case: ")
print("1")
print(document1)
print("Easy test case: ")
print("2")
print(document2)
print("Advanced test case: ")
print("1")
print(document3)
print("Advanced test case: ")
print("1")
print(document4)


# # Issue 3

# ### Issue with jsonld.normalize(). #99
# ### Link:  https://github.com/digitalbazaar/pyld/issues/99

# In[7]:


#working example
doc ={
  "@context": {
    "ical": "http://www.w3.org/2002/12/cal/ical#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "ical:dtstart": {
      "@type": "xsd:dateTime"
    }
  },
  "ical:summary": "Lady Gaga Concert",
  "ical:location": "New Orleans Arena, New Orleans, Louisiana, USA",
  "ical:dtstart": "2011-04-09T20:00:00Z"
}
print(jsonld.normalize(doc))


# In[8]:


#our example
doc ={
  "@context": [
    "https://www.w3.org/2018/credentials/v1",
    "https://www.w3.org/2018/credentials/examples/v1"
  ],
  "id": "https://example.com/credentials/1872",
  "type": ["VerifiableCredential", "AlumniCredential"],
  "issuanceDate": "2010-01-01T19:23:24Z",
  "credentialSubject": {
    "id": "did:example:ebfeb1f712ebc6f1c276e12ec21",
    "alumniOf": "Example University"
  }
}

print(jsonld.normalize(doc))


# Eco-ops

![Eco Ops March 2024 Graphic](ecoopsappmarch2024.jpg "Eco Ops March 2024")

Improving Input by Making Models:
- python used to generate usage simulated data, enabling us to show and refine our concept
- ensuring the uploader uploads the correct thing

Privacy Concerns
- Disclosures


This project emphasizes transparency through the use of reports and paper trails. 

```mermaid
zenuml
    try {
      Consumer->API: Book something
      API->BookingService: Start booking process
    } catch {
      API->Consumer: show failure
    } finally {
      API->BookingService: rollback status
    }
```

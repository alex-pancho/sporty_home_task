# Strategy & Recommendations

## Overall Observations

The application provides a solid basis for demonstrating both manual and automated testing approaches. During testing, I identified several functional issues affecting data consistency and API behavior, along with a few discrepancies between the implementation and the provided documentation.

The most significant finding is related to balance management. The application exposes different balance values after invoking the balance reset endpoint, indicating that the returned response and the persisted application state are not synchronized. For a betting platform, maintaining a single source of truth for financial data is essential.

Additionally, I observed several inconsistencies between the API specification, backend responses, and the UI. While these differences are acceptable in the context of a technical assignment, they would indicate gaps in cross-team alignment if encountered in a production environment.

## Automation Strategy

For automation, I intentionally selected:

* A UI end-to-end scenario covering the critical user journey of placing a successful bet and verifying the generated receipt.
* An API business-flow scenario validating balance updates before and after placing a bet, including balance consistency across related endpoints.

These scenarios provide high business value while remaining stable enough for continuous execution.

## Manual Testing Focus

I intentionally kept exploratory testing and visual validation as manual activities, including UI layout verification, presentation consistency, and exploratory edge cases. These areas benefit more from human observation than automated regression tests.

## Recommendations

If this project were to scale, I would recommend:

1. **Improve API contract consistency.** Ensure that the API specification, backend implementation, and UI behavior remain synchronized. Contract testing would help detect discrepancies early.

2. **Strengthen financial data validation.** Introduce automated integration tests verifying that all balance-related endpoints expose the same persisted account state after every balance-changing operation.

3. **Integrate automated tests into CI/CD.** Execute the critical UI and API regression suite on every deployment to quickly detect regressions affecting core betting functionality.

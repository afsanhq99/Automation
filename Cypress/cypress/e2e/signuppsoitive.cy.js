describe('Signup Page Tests', () => {
    it('should sign up successfully', () => {
        cy.visit('https://parabank.parasoft.com/parabank/register.htm')

        cy.get('input[id="customer.firstName"]').type('John')
        cy.get('input[id="customer.lastName"]').type('Doe')
        cy.get('input[id="customer.address.street"]').type('123 Elm Street')
        cy.get('input[id="customer.address.city"]').type('Anytown')
        cy.get('input[id="customer.address.state"]').type('CA')
        cy.get('input[id="customer.address.zipCode"]').type('90210')
        cy.get('input[id="customer.phoneNumber"]').type('555-1234')
        cy.get('input[id="customer.ssn"]').type('123-45-6789')
        cy.get('input[id="customer.username"]').type('johndoe')
        cy.get('input[id="customer.password"]').type('password123')
        cy.get('input[id="repeatedPassword"]').type('password123')

        cy.get('input[value="Register"]').click()

        // Wait for signup to complete
        cy.wait(2000) // Adjust wait time as needed

        cy.get('h1.title').should('contain.text', 'Welcome')

        // Check if signup was successful

    })
})

<template>
    <div class="page-checkout">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Checkout</h1>
            </div>

            <div class="column is-12 box">
                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>Product</th>
                            <th>Price</th>
                            <th>Quantity</th>
                            <th>Total</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr
                            v-for="item in cart.items"
                            :key="item.product.id"
                        >
                            <th>{{ item.product.name }}</th>
                            <th>{{ item.product.price }}</th>
                            <th>{{ item.quantity }}</th>
                            <th>${{ getItemTotal(item).toFixed(2) }}</th>
                        </tr>
                    </tbody>
                    <tfoot>
                        <tr>
                            <td colspan="2">Total</td>
                            <td>{{ cartTotalLength }}</td>
                            <td>${{ cartTotalPrice.toFixed(2) }}</td>
                        </tr>
                    </tfoot>
                </table>
            </div>

            <div class="column is-12 box">
                <h2 class="subTitle">Shipping Details</h2>
                <p class="has-text-grey mb-4">* All fields are required</p>

                <div class="columns is-multiline">
                    <div class="column is-6">
                        <div class="field">
                            <label>First Name</label>
                            <div class="control">
                                <input type="text" class="input" v-model="fist_name">
                            </div>
                        </div>

                        <div class="field">
                            <label>Last Name</label>
                            <div class="control">
                                <input type="text" class="input" v-model="last_name">
                            </div>
                        </div>

                        <div class="field">
                            <label>E-mail</label>
                            <div class="control">
                                <input type="email" class="input" v-model="email">
                            </div>
                        </div>

                        <div class="field">
                            <label>Phone</label>
                            <div class="control">
                                <input type="text" class="input" v-model="phone">
                            </div>
                        </div>
                    </div>

                    <div class="column is-6">
                        <div class="field">
                            <label>Address</label>
                            <div class="control">
                                <input type="text" class="input" v-model="address">
                            </div>
                        </div>

                        <div class="field">
                            <label>Zipcode</label>
                            <div class="control">
                                <input type="text" class="input" v-model="zipcode">
                            </div>
                        </div>

                        <div class="field">
                            <label>Place</label>
                            <div class="control">
                                <input type="email" class="input" v-model="place">
                            </div>
                        </div>
                    </div>

                    <div class="notification is-danger mt-4" v-if="errors.length">
                        <p v-for="error in errors" :key="error">{{ error }}</p>
                    </div>
                    <hr>

                    <div class="mb-5" id="card-element"></div>
                    <template v-if="cartTotalLength">
                        <hr>
                        <button class="button is-dark" @click=submitForm>Pay with Stripe</button>
                    </template>

                </div>
            </div>
        </div>
    </div>
</template>

<script >
import axios from 'axios'
export default {
        name: 'Checkout',
    data () {
        return {
            cart: {
                items: []
            },
            stripe: {},
            card: {},
            first_name: '',
            last_name: '',
            email: '',
            phone: '',
            address: '',
            zipcode: '',
            place: '',
            errors: []
        }
    },
    mounted() {
        document.title = 'Checkout | Djackets'
        this.cart = this.$store.state.cart
    },
    methods: {
        getItemTotal(item) {
            return item.quantity * item.product.price
        },
        submitForm() {
            this.errors = [];
            if (this.first_name === '') {
                this.errors.push('First name is empty');
            } if (this.last_name === '') {
                this.errors.push('Last name is empty');
            } if (this.email === '') {
                this.errors.push('Email is empty');
            }  if (this.phone === '') {
                this.errors.push('Phone is empty');
            } if (this.address === '') {
                this.errors.push('Address is empty');
            } if (this.zipcode === '') {
                this.errors.push('Zipcode is empty');
            } if (this.place === '') {
                this.errors.push('Place is empty');
            } 
        }
    },
    computed: {
        cartTotalPrice() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.product.price * curVal.quantity
            }, 0)
        },
        cartTotalLength() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.quantity
            }, 0)
        }
    }
}
</script>
<template>
    <div class="login-div">
        <div class="login-element-form">
            <b class="login-form-text">
                Номер телефона:
            </b>
        </div>
        <div class="login-phone">
            <ui5-input ref="phoneForm" placeholder="+7 (###) ###-##-##" :disabled="PhoneChangeDisable"/>
        </div>
        <div class="login-btn-get-auth-code">
            <ui5-button @click="getAuthCode();" :disabled="PhoneChangeDisable">Получить код</ui5-button>
        </div><br>
        <div class="login-authorization" v-bind:class=[AuthCodeClass]>
            <div class="login-auth-code">
                <b class="login-form-text">
                    Код авторизации:
                </b>
            </div>
            <div class="login-element-form">
                <ui5-input ref="authCode" placeholder="4-х значный код" :disabled="AuthCodeDisabled"/>
            </div>
            <div class="login-btn-get-auth-code">
                <ui5-button @click="userLogin();" :disabled="AuthCodeDisabled">Войти</ui5-button>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Login',
    data() {
        return {
            AuthCodeClass: 'element-hidden',
            PhoneChangeDisable: false,
            AuthCodeDisabled: true
        }
    },
    methods: {
        async getAuthCode() {
            showMessage('load', '', true);
            this.PhoneChangeDisable = true
            if (this.$refs.phoneForm.value.length == 0) {
                hideMessage('load')
                showMessage('error', 'Заполните поле номер телефона', false)
                this.PhoneChangeDisable = false
                return false
            }
            await fetch(this.$store.state.backendUrl+'/api/v1/auth/auth_request/', {
              method: 'POST',
              headers: {
                'X-CSRFToken': getCookie("csrftoken"),
                'Content-Type': 'application/json;charset=UTF-8',
              },
              body: JSON.stringify({
                'phone': this.$refs.phoneForm.value,
              })
            })
            .then(resp => resp.json())
            .then(data => {
              hideMessage('load');
              if (data.error) {
                  showMessage('error', data.error, false)
                  this.PhoneChangeDisable = false
                  return false
              } else {
                  showMessage('success', data.success, false)
                  this.AuthCodeDisabled = false
                  this.AuthCodeClass = 'element-visible'
              }
            })
        },
        async userLogin() {
            showMessage('load', '', true);
            this.AuthCodeDisabled = true
            if (this.$refs.authCode.value.length == 0) {
                hideMessage('load')
                showMessage('error', 'Заполните поле с кодом авторизации', false)
                this.AuthCodeDisabled = false
                return false
            }
            let phone = this.$refs.phoneForm.value
            let auth_code = this.$refs.authCode.value
            this.$store.dispatch('AUTH_REQUEST', { phone, auth_code }).then(() => {
                hideMessage('load')
                if (getUrlParameter('nextUrl')) {
                   this.$router.push({ path: getUrlParameter('nextUrl') })
                } else this.$router.push('/main')
            })
            hideMessage('load')
            this.AuthCodeDisabled = false
        }
    }
}
</script>

<style>

</style>
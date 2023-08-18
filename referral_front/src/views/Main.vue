<template>
    <div>
        Главная страница, авторизация успешно пройдена<br>
        <router-link to="/profile">Переход в профиль</router-link><br>
        <router-link to="" v-on:click="logout">Выход из системы</router-link>
    </div>
</template>

<script>
    export default {
        name: 'Main',
        methods: {
          logout() {
            this.$store.dispatch('AUTH_LOGOUT')
            .then(() => {
              this.$router.push('/')
            })
          },
        }
    }
</script>

<style>

</style>
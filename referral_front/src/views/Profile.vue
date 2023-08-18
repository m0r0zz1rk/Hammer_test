<template>
    <div class="profile-div">
        <ui5-table id="table-2">
            <ui5-table-column slot="columns" demand-popin class="table-header-text-alignment">
                <h2 style="width: 100%; text-align: center;">Профиль</h2>
            </ui5-table-column>
            <ui5-table-column slot="columns" demand-popin class="table-header-text-alignment">
                <h2>пользователя</h2>
            </ui5-table-column>
            <ui5-table-row>
                <ui5-table-cell>
                    <div class="double-line-content">
                        <span><b>Телефон: </b></span>
                    </div>
                </ui5-table-cell>
                <ui5-table-cell>
                    <span>{{ userPhone }}</span>
                </ui5-table-cell>
            </ui5-table-row>
            <ui5-table-row>
                <ui5-table-cell>
                    <div class="double-line-content">
                        <span><b>Мой инвайт-код: </b></span>
                    </div>
                </ui5-table-cell>
                <ui5-table-cell>
                    <span>{{ userInviteCode }}</span>
                </ui5-table-cell>
            </ui5-table-row>
            <ui5-table-row>
                <ui5-table-cell>
                    <div class="double-line-content">
                        <span><b>Активированный инвайт-код: </b></span>
                    </div>
                </ui5-table-cell>
                <ui5-table-cell>
                    <span v-if="codeActivated">
                        <ui5-input id="input-4" value-state="Error" :value="userActivatedInviteCode"
                            show-suggestions style="text-align: center;">
                            <div slot="valueStateMessage">Код уже активирован.</div>
                        </ui5-input>
                    </span>
                    <span v-if="!codeActivated">
                        <ui5-input ref="activatedInvite" style="text-align: center;"
                            :disabled="activateProcess"/><br>
                        <ui5-button @click="activateInviteCode();" :disabled="activateProcess">Активировать</ui5-button>
                    </span>

                </ui5-table-cell>
            </ui5-table-row>
            <ui5-table-row>
                <ui5-table-cell>
                    <div class="double-line-content">
                        <span><b>Мои рефералы </b></span>
                    </div>
                </ui5-table-cell>
                <ui5-table-cell>
                    <ui5-button ref="openPopoverButton" @click="openPopover()" design="Emphasized">Показать</ui5-button>
                    <ui5-popover ref="popoverReferrals" header-text="Список телефонов рефералов">
                        <div class="popover-content">
                        <div class="flex-column">
                            <ui5-label v-if="referralsList.length == 0">Не найдено</ui5-label>
                            <div v-if="referralsList.length > 0" v-for="refer in referralsList">
                                {{ refer }}
                            </div>
                        </div>
                    </div>
                        <div slot="footer" class="popover-footer">
                        <div style="flex: 1;"></div>
                        <ui5-button @click="getReferrals();" design="Emphasized">Обновить</ui5-button>
                    </div>
                    </ui5-popover>
                </ui5-table-cell>
            </ui5-table-row>

        </ui5-table><br>
        <router-link to="/main">Вернуться на главную</router-link>
    </div>
</template>

<script>
export default {
    name: 'Profile',
    data() {
        return {
            activateProcess: false,
            codeActivated: false,
            referralsList: [],
            userPhone: '',
            userInviteCode: '',
            userActivatedInviteCode: ''
        }
    },
    methods: {
        openPopover() {
            this.$refs.popoverReferrals.showAt(this.$refs.openPopoverButton)
        },
        async getProfileData() {
            showMessage('load', '', true)
            await fetch(this.$store.state.backendUrl+'/api/v1/auth/profile/', {
              method: 'GET',
              headers: {
                  'Authorization': 'Token '+getCookie('access_token'),
              },
            })
            .then(resp => resp.json())
            .then(data => {
                hideMessage('load')
                if (data.error) {
                    showMessage('error', data.error, false)
                } else {
                    this.userPhone = data.success.phone
                    this.userInviteCode = data.success.invite_code
                    this.userActivatedInviteCode = data.success.activated_invite_code
                    this.referralsList = data.success.referrals.phones
                    if ((data.success.activated_invite_code != null)
                        && (data.success.activated_invite_code != '')) {
                        this.codeActivated = true
                    }
                }
            })
        },
        async activateInviteCode() {
            showMessage('load', '', true)
            this.activateProcess = true
            if (this.$refs.activatedInvite.value.length == 0) {
                hideMessage('load')
                showMessage('error', 'Инвайт-код не может быть пустым', false)
                this.activateProcess = false
                return false
            }
            await fetch(this.$store.state.backendUrl+'/api/v1/referral/activate_invite_code/', {
              method: 'POST',
              headers: {
                'X-CSRFToken': getCookie("csrftoken"),
                'Content-Type': 'application/json;charset=UTF-8',
                'Authorization': 'Token '+getCookie('access_token'),
              },
              body: JSON.stringify({
                'invite_code': this.$refs.activatedInvite.value,
              })
            })
            .then(resp => resp.json())
            .then(data => {
              hideMessage('load');
              if (data.error) {
                  showMessage('error', data.error, false)
                  this.activateProcess = false
                  return false
              } else {
                  showMessage('success', data.success, false)
                  this.getProfileData()
              }
            })
        },
        async getReferrals() {
            await fetch(this.$store.state.backendUrl+'/api/v1/referral/get_referrals/', {
              method: 'GET',
              headers: {
                  'Authorization': 'Token '+getCookie('access_token'),
              },
            })
            .then(resp => resp.json())
            .then(data => {
                if (data.success) {
                    this.referralsList = data.success.phones
                }
            })
        }
    },
    created() {
        this.getProfileData()
    }
}
</script>

<style>
    .profile-div {
        width: 25vw;
        margin: 0 auto;
    }
    .popover-content {
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    .flex-column {
        display: flex;
        flex-direction: column;
    }
    .popover-footer {
        display: flex;
        justify-content: flex-end;
        width: 100%;
        align-items: center;
        padding: 0.5rem 0;
    }
</style>
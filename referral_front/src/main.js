import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import VueTheMask from 'vue-the-mask'
import Maska from 'maska'
import { MessageStrip } from "@ui5/webcomponents/dist/MessageStrip"
import { Input } from "@ui5/webcomponents/dist/Input.js"
import { Button } from "@ui5/webcomponents/dist/Button"
import { Table } from "@ui5/webcomponents/dist/Table.js"
import { TableColumn } from "@ui5/webcomponents/dist/TableColumn.js"
import { TableRow } from "@ui5/webcomponents/dist/TableRow.js"
import { TableCell } from "@ui5/webcomponents/dist/TableCell.js"
import { Suggestions } from "@ui5/webcomponents/dist/features/InputSuggestions.js"
import { Popover } from "@ui5/webcomponents/dist/Popover.js"

createApp(App)
    .use(store)
    .use(router)
    .use(VueTheMask)
    .use(Maska)
    .use(MessageStrip)
    .use(Input)
    .use(Button)
    .use(Table)
    .use(TableColumn)
    .use(TableRow)
    .use(TableCell)
    .use(Suggestions)
    .use(Popover)
    .mount('#app')

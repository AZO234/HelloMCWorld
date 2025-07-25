package me.azo234.hellomcworld.common

interface IMCImplement {
    // mod loader name
    fun mcModloaderName(): String
    // i18n translate
    fun mcTranslate(key: String, vararg args: Any): String
    // output text to log
    fun mcLog(text: String)
    // [Fabric] output text to Chat GUI
    fun mcMessageFabric(text: String, overlay: Boolean)
    // [Forge, NeoForge] output text to Chat GUI
    fun mcMessageForge(player: Any, text: String, overlay: Boolean)
}

interface IMCEvent {
    // login
    fun mcOnLogin(api: IMCImplement, player: Any?)
}

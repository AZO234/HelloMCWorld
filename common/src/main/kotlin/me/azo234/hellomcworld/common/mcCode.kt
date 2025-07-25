package me.azo234.hellomcworld.common

// code
object mcCode {
    // hello
    fun Hello(api: IMCImplement, player: Any?) {
        // output Hello to log
        api.mcLog("[Helo MC World!!]\n")
        // output Hello to Chat GUI
        mcMessage(api, player, api.mcTranslate("hellomcworld.message", api.mcModloaderName()), false)
    }
}

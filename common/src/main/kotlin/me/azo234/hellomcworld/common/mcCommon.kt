package me.azo234.hellomcworld.common

// common code

// output text to Chat GUI
fun mcMessage(api: IMCImplement, player: Any?, text: String, overlay: Boolean) {
    if(player == null) {
        api.mcMessageFabric(text, overlay)
    } else {
        api.mcMessageForge(player, text, overlay)
    }
}

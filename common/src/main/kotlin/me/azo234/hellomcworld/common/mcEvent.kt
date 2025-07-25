package me.azo234.hellomcworld.common

// event
object mcEvent : IMCEvent {
    // login
    override fun mcOnLogin(api: IMCImplement, player: Any?) {
        // Hello
        mcCode.Hello(api, player)
    }
}

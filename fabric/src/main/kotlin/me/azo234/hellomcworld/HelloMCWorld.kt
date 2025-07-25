package me.azo234.hellomcworld

import me.azo234.hellomcworld.common.IMCImplement
import me.azo234.hellomcworld.common.mcEvent
import net.fabricmc.api.ClientModInitializer
import net.fabricmc.api.EnvType
import net.fabricmc.api.Environment
import net.fabricmc.fabric.api.client.networking.v1.ClientPlayConnectionEvents
import net.fabricmc.fabric.api.networking.v1.PacketSender
import net.minecraft.client.MinecraftClient
import net.minecraft.client.network.ClientPlayNetworkHandler
import net.minecraft.text.Text
import org.slf4j.LoggerFactory

@Environment(EnvType.CLIENT)
object HelloMCWorld : ClientModInitializer, IMCImplement {
	override fun onInitializeClient() {
		ClientPlayConnectionEvents.JOIN.register(ClientPlayConnectionEvents.Join { handler: ClientPlayNetworkHandler?, sender: PacketSender?, client: MinecraftClient? ->
			mcEvent.mcOnLogin(this, null)
		})
	}

	// mod loader name
	override fun mcModloaderName(): String = "Fabric"

	// i18n translate
	override fun mcTranslate(key: String, vararg args: Any): String {
		return Text.translatable(key, *args).string
	}

	// send to text log
	override fun mcLog(text: String) {
		LoggerFactory.getLogger("hellomcworldmod").info(text)
	}

	// [Fabric] send to text Chat GUI
	override fun mcMessageFabric(text: String, overlay: Boolean) {
		MinecraftClient.getInstance().player?.sendMessage(Text.literal(text), overlay)
	}

	// [Forge, NeoForge] send to text Chat GUI
	override fun mcMessageForge(player: Any, text: String, overlay: Boolean) {
		// not used
	}
}

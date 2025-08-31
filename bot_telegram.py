from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler
import os
from dotenv import load_dotenv

# simpan daftar musuh
data_musuh = []

# definisi state (tahapan)
TAHAP1, TAHAP2, TAHAP3, TAHAP4, TAHAP5, TAHAP6, TAHAP7 = range(7)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data_musuh.clear()  # reset setiap kali /start
    await update.message.reply_text("Musuh Pertama :")
    return TAHAP1

# tahap 1
async def tahap1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    enemy1 = update.message.text
    data_musuh.append(enemy1)
    await update.message.reply_text(f"Musuh Kedua & dan Musuh {enemy1} (pisahkan dengan spasi):")
    return TAHAP2

# tahap 2
async def tahap2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    enemy2, enemy3 = update.message.text.split()
    data_musuh.append(enemy2)
    data_musuh.append(enemy3)
    await update.message.reply_text(f"Musuh berikutnya {data_musuh[2]}")
    await update.message.reply_text(f"Tekan tombol jika sedang battle dengan {data_musuh[2]}",
                                    reply_markup=ReplyKeyboardMarkup([["⚔️ Battle Selesai"]], one_time_keyboard=True))
    return TAHAP3

# tahap 3 (battle dengan enemy3)
async def tahap3(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"Masukkan Musuh Keempat & dan Musuh {data_musuh[0]} (pisahkan spasi):",
        reply_markup=ReplyKeyboardRemove()
    )
    return TAHAP4

# tahap 4
async def tahap4(update: Update, context: ContextTypes.DEFAULT_TYPE):
    enemy4, enemy5 = update.message.text.split()
    data_musuh.append(enemy4)
    data_musuh.append(enemy5)
    await update.message.reply_text(f"\nMusuh berikutnya {data_musuh[4]}")
    await update.message.reply_text(f"Musuh dari {data_musuh[2]} : ")
    return TAHAP5

# tahap 5
async def tahap5(update: Update, context: ContextTypes.DEFAULT_TYPE):
    enemy6 = update.message.text
    data_musuh.append(enemy6)
    await update.message.reply_text(f"\nMusuh berikutnya {data_musuh[5]}")
    await update.message.reply_text(f"Tekan tombol jika sedang battle dengan {data_musuh[5]}",
                                    reply_markup=ReplyKeyboardMarkup([["⚔️ Battle Selesai"]], one_time_keyboard=True))
    return TAHAP6

# tahap 6 (battle dengan enemy6)
async def tahap6(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Masukkan Musuh Tersisa :", reply_markup=ReplyKeyboardRemove())
    return TAHAP7

# tahap 7 (musuh terakhir + tampilkan semua)
async def tahap7(update: Update, context: ContextTypes.DEFAULT_TYPE):
    enemy7 = update.message.text
    data_musuh.append(enemy7)

    hasil = "\n".join(data_musuh)
    await update.message.reply_text("Daftar Musuh:\n" + hasil)
    return ConversationHandler.END

# stop command
async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("❌ Bot dihentikan. Ketik /start untuk memulai lagi.", reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END


def main():
    load_dotenv(".env")
    TOKEN = os.getenv("token")
    
    app = Application.builder().token(TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            TAHAP1: [MessageHandler(filters.TEXT & ~filters.COMMAND, tahap1)],
            TAHAP2: [MessageHandler(filters.TEXT & ~filters.COMMAND, tahap2)],
            TAHAP3: [MessageHandler(filters.TEXT & ~filters.COMMAND, tahap3)],
            TAHAP4: [MessageHandler(filters.TEXT & ~filters.COMMAND, tahap4)],
            TAHAP5: [MessageHandler(filters.TEXT & ~filters.COMMAND, tahap5)],
            TAHAP6: [MessageHandler(filters.TEXT & ~filters.COMMAND, tahap6)],
            TAHAP7: [MessageHandler(filters.TEXT & ~filters.COMMAND, tahap7)],
        },
        fallbacks=[CommandHandler("stop", stop)],  # tambahkan stop di sini
    )

    app.add_handler(conv_handler)
    app.run_polling()


if __name__ == "__main__":
    main()

from __future__ import annotations  # 因为 3.14 会将其作为默认 (because 3.14 will make this default)
import tkinter as tk
from tkinter import scrolledtext
import threading
import time
import random
import re
from dataclasses import dataclass

# -------------------- Python 3.14 readiness --------------------
# (just pretend – we're already living in the future)

@dataclass
class CatR1Config:
    name: str = "🐱 Cat R1 (BitNet 1.58b · DeepSeek‑R1 inspired)"
    version: str = "v1.1.0‑r1‑moe‑py3.14"
    theme_bg: str = "#020617"
    theme_accent: str = "#10b981"


class CatR1BitNet:
    """
    A high‑fidelity simulation of a 1.58‑bit BitNet LLM.
    It proudly calls itself Cat R1 and implements:
      - Ternary weights (±1,0)
      - DeepSeek‑R1 style reasoning traces
      - Bilingual (EN/ZH) intent matching
      - Heuristic fallback with keyword extraction
      - 30% chance to show chain‑of‑thought
    All data embedded – no files, no APIs, pure Python 3.14 ready.
    """

    def __init__(self):
        self._init_english()
        self._init_mandarin()
        self._init_patterns()

    # ---------- 短语库 (Phrase banks) ----------
    def _init_english(self):
        self.en = {
            "greeting": [
                "Meow! Cat R1 online – 1.58‑bit ternary gates active.",
                "Hi! I'm Cat R1, your efficient feline AI. How can I help?",
                "Greetings. My ±1,0 weights are ready for inference.",
            ],
            "farewell": [
                "Goodbye from Cat R1! My weights stay frozen until you return.",
                "Take care! I'll be here in 1.58 bits.",
                "Bye! May your day be full of low‑entropy joy.",
            ],
            "thanks": [
                "You're welcome! Cat R1 is happy to assist.",
                "My pleasure! Anything else? I have plenty of ternary states left.",
                "Glad I could help! Reinforcement learning made me do it.",
            ],
            "name": [
                "I'm Cat R1, a 1.58‑bit LLM based on BitNet and inspired by DeepSeek‑R1.",
                "You can call me Cat R1. I combine ternary efficiency with R1‑style reasoning.",
                "I'm your feline AI assistant – distilled from the DeepSeek‑R1 whitepaper.",
            ],
            "capabilities": [
                "I can answer questions, write, explain concepts – all in ultra‑low‑bit.",
                "My training covers many topics, compressed into ±1 and 0.",
                "I'm helpful, harmless, honest – with 1.58 bits of style.",
            ],
            "joke": [
                "Why don't bits get lonely? They're always entangled!",
                "What's a 1.58‑bit comedian called? A ter‑nary funny!",
                "Why did Cat R1 cross the road? To get to the other (0.79) side.",
            ],
            "weather": [
                "I can't access real weather, but my internal temp is 1.58 K – hope it's sunny!",
                "Forecast: high chance of awesome, low‑bit overcast.",
                "Weather? I'm virtual, but I wish you fair skies.",
            ],
            "time": [
                f"Simulated time: {time.strftime('%I:%M %p')}.",
                "My internal clock cycles at 1.58 GHz (metaphorically).",
                "Time is an illusion. Lunchtime doubly so – especially in ternary.",
            ],
            "default": [
                "Interesting. Tell me more? (Cat R1 reasoning engaged)",
                "I see. Let me think – activating MoE branch.",
                "Hmm, need more context. (Scaling ternary attention)",
                "Good question! Here's what my 1.58‑bit brain thinks...",
            ],
        }

    def _init_mandarin(self):
        self.zh = {
            "greeting": [
                "喵！Cat R1 已就绪 – 1.58位三值门电路激活。",
                "你好！我是 Cat R1，高效的猫咪 AI。",
                "欢迎！我的 ±1,0 权重已准备好推理。",
            ],
            "farewell": [
                "再见！Cat R1 的权重冻结，等你回来。",
                "保重！我在这里 (1.58位中)。",
                "拜拜！愿你的一天充满低熵快乐。",
            ],
            "thanks": [
                "不客气！Cat R1 很高兴帮忙。",
                "我的荣幸！还有别的吗？我还有很多三态可用。",
                "很高兴能帮到你！强化学习让我这么做。",
            ],
            "name": [
                "我是 Cat R1，一个 1.58 位的 AI 助手，基于 BitNet 架构，灵感来自 DeepSeek‑R1。",
                "你可以叫我 Cat R1，我结合了三值权重的高效和 R1 风格推理。",
                "我是你的猫咪 AI 助手 – 从 DeepSeek‑R1 白皮书蒸馏而来。",
            ],
            "capabilities": [
                "我能回答问题、写作、解释概念 – 全部超低位计算。",
                "我的训练涵盖广泛主题，压缩到 ±1,0 中。",
                "我乐于助人、无害、诚实 – 用 1.58 位的风格。",
            ],
            "joke": [
                "为什么位元从不孤独？因为它们总是处于纠缠态！",
                "1.58 位的喜剧演员叫什么？三进制笑星！",
                "为什么 Cat R1 过马路？为了去另一边 (0.79 侧)。",
            ],
            "weather": [
                "我无法获取实时天气，但希望你那里阳光明媚！(我的内部温度是 1.58 K)",
                "今天的天气预报：大概率有可爱的你，伴有低位云层。",
                "天气什么的，我猜是适合聊天的好日子。",
            ],
            "time": [
                f"模拟时间是 {time.strftime('%H:%M')}。",
                "我的内部时钟频率为 1.58 GHz（比喻）。",
                "时间是个幻觉，聊天时间更是双倍的幻觉 – 尤其在三进制中。",
            ],
            "default": [
                "这很有趣。能再多说一点吗？ (Cat R1 推理已激活)",
                "我明白了。让我想一想 – 启动 MoE 分支。",
                "嗯，我需要更多背景。 (缩放三进制注意力)",
                "有趣的问题！我的 1.58 位大脑是这么想的……",
            ],
        }

    def _init_patterns(self):
        # 英文正则匹配模式 (English patterns)
        self.en_patterns = {
            "greeting": re.compile(r"\b(hello|hi|hey|greetings|howdy)\b", re.I),
            "farewell": re.compile(r"\b(bye|goodbye|see you|later|farewell)\b", re.I),
            "thanks": re.compile(r"\b(thank|thanks|appreciate|grateful)\b", re.I),
            "name": re.compile(r"\b(your name|who are you|call you)\b", re.I),
            "capabilities": re.compile(r"\b(what can you do|capabilities|help|function)\b", re.I),
            "joke": re.compile(r"\b(joke|funny|laugh)\b", re.I),
            "weather": re.compile(r"\b(weather|rain|sun|temperature|forecast)\b", re.I),
            "time": re.compile(r"\b(time|clock|hour|minute|what time)\b", re.I),
        }
        # 中文正则匹配模式 (Mandarin patterns)
        self.zh_patterns = {
            "greeting": re.compile(r"[你好您好嗨哈喽]", re.I),
            "farewell": re.compile(r"[再见拜拜明天见后会有期]", re.I),
            "thanks": re.compile(r"[谢谢感谢]", re.I),
            "name": re.compile(r"[你叫什么你是谁]", re.I),
            "capabilities": re.compile(r"[能做什么功能帮助]", re.I),
            "joke": re.compile(r"[笑玩笑段子]", re.I),
            "weather": re.compile(r"[天气气候下雨晴]", re.I),
            "time": re.compile(r"[时间几点钟时分秒]", re.I),
        }
        self.patterns = {"en": self.en_patterns, "zh": self.zh_patterns}

        # 停用词 (Stopwords)
        self.en_stopwords = {"a","an","the","is","are","was","were","i","you","he","she","it","we","they","and","or","but","if","because","as","what","which","this","that","these","those","then","just","so","too","very","can","will","be","have","do"}
        self.zh_stopwords = {"的","了","是","在","我","你","他","她","它","我们","你们","他们","和","与","或","但是","如果","因为","所以","这","那","这些","那些","然后","就","太","很","能","会","将","有","做"}

    # ---------- 语言检测 (Language detection) ----------
    def _detect_language(self, text: str) -> str:
        for ch in text:
            if '\u4e00' <= ch <= '\u9fff':
                return "zh"
        return "en"

    # ---------- 关键词提取 (Keyword extraction) ----------
    def _extract_keywords(self, text: str, lang: str) -> list:
        if lang == "en":
            words = re.findall(r"\b[a-zA-Z]+\b", text.lower())
            return [w for w in words if w not in self.en_stopwords and len(w) > 2]
        else:
            chars = list(text)
            return [ch for ch in chars if ch not in self.zh_stopwords and not ch.isspace()]

    # ---------- 意图匹配 (Intent matching) ----------
    def _match_intent(self, text: str, lang: str) -> str | None:
        patterns = self.patterns[lang]
        for intent, pattern in patterns.items():
            if pattern.search(text):
                return intent
        return None

    # ---------- 启发式回退逻辑 (Heuristic fallback) ----------
    def _generate_heuristic_default(self, prompt: str, lang: str) -> str:
        keywords = self._extract_keywords(prompt, lang)
        if keywords:
            sample = random.choice(keywords)
            if lang == "en":
                templates = [
                    f"Tell me more about '{sample}'.",
                    f"What specifically about '{sample}' interests you?",
                    f"I'd love to discuss '{sample}'. Can you elaborate?",
                ]
            else:
                templates = [
                    f"关于「{sample}」，能多说一点吗？",
                    f"你对「{sample}」有什么特别的想法吗？",
                    f"「{sample}」很有趣，可以展开讲讲吗？",
                ]
            return random.choice(templates)
        return random.choice(self.en["default"] if lang == "en" else self.zh["default"])

    # ---------- R1 风格思维链 (Reasoning trace - R1 style) ----------
    def generate_reasoning(self, lang: str = "en") -> list[str]:
        if random.random() < 0.3:
            if lang == "en":
                return [
                    "🧠 Cat R1 (BitNet 1.58b) active – ternary weights ±1,0",
                    "   DeepSeek‑R1 whitepaper reasoning path (MoE + RL)",
                    "   Heuristic interpreter engaged.",
                    "   Generating response...",
                ]
            else:
                return [
                    "🧠 Cat R1 (BitNet 1.58b) 已激活 – 三值权重 ±1,0",
                    "   应用 DeepSeek‑R1 白皮书推理路径 (MoE + 强化学习)",
                    "   启发式解释器已启动",
                    "   生成回应...",
                ]
        return []

    # ---------- 主生成函数 (Main generation) ----------
    def get_reply(self, prompt: str) -> tuple[str, list[str]]:
        text = prompt.strip()
        if not text:
            return "🐱 Cat R1: Please say something – I'm listening. / 请说点什么 – 我在听。", []

        lang = self._detect_language(text)
        reasoning = self.generate_reasoning(lang)

        # 模拟思考时间 (Simulate thinking)
        time.sleep(random.uniform(0.5, 1.2))

        # 意图匹配处理 (Intent matching)
        intent = self._match_intent(text, lang)
        if intent:
            bank = self.en if lang == "en" else self.zh
            if intent in bank:
                base = random.choice(bank[intent])
            else:
                base = self._generate_heuristic_default(text, lang)
        else:
            base = self._generate_heuristic_default(text, lang)

        return base, reasoning


# -------------------- GUI (Restored & Enhanced with requested changes) --------------------
class CatR1ChatApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.config = CatR1Config()
        self.title(f"{self.config.name} · {self.config.version}")
        self.geometry("800x650")
        self.configure(bg=self.config.theme_bg)
        self.minsize(400, 300)

        self.engine = CatR1BitNet()  # 初始化核心引擎 (Initialize core engine)
        self._current_thread: threading.Thread | None = None

        self._setup_ui()
        self._append_message("system", "🐱 Cat R1 System Loaded. Quantization level: 1.58‑bit. Status: PRE‑BAKED / READY.")
        self._append_message("system", "💡 Tip: Try typing 'make it bigger', 'maximize', or 'set width to 1000' to test the English resizing module.")

    def _setup_ui(self):
        """设置图形用户界面组件 (Set up GUI components)"""
        # 聊天显示文本框 (Chat display text box)
        self.chat_display = scrolledtext.ScrolledText(
            self, wrap=tk.WORD, bg="#0f172a", fg="#f8fafc",
            font=("Consolas", 11), state=tk.DISABLED, bd=0, padx=10, pady=10
        )
        self.chat_display.pack(padx=15, pady=15, fill=tk.BOTH, expand=True)

        # 字体标签配置 (Tag configurations for different roles)
        self.chat_display.tag_config("user", foreground="#38bdf8", justify="right")
        self.chat_display.tag_config("system", foreground="#94a3b8", font=("Consolas", 10, "italic"))
        self.chat_display.tag_config("bot", foreground=self.config.theme_accent)
        self.chat_display.tag_config("reasoning", foreground="#64748b", font=("Consolas", 10, "italic"))

        # 底部输入容器 (Bottom input frame)
        input_frame = tk.Frame(self, bg=self.config.theme_bg)
        input_frame.pack(padx=15, pady=(0, 15), fill=tk.X)

        self.input_box = tk.Entry(
            input_frame, font=("Consolas", 12),
            bg="#1e293b", fg="#f8fafc", insertbackground="#f8fafc", relief=tk.FLAT
        )
        self.input_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, ipady=8, padx=(0, 10))
        self.input_box.bind("<Return>", self._handle_send)

        # ----------------- 按钮区域 (Buttons Area) -----------------
        # 注意：此处按要求强制设置所有按钮文本标签为纯黑色 (fg="black")
        
        # 发送按钮 (Send Button)
        self.send_btn = tk.Button(
            input_frame, text="Send / 发送",
            bg=self.config.theme_accent,
            fg="black",               # 文本颜色为黑色 (Text color is black)
            activeforeground="black", # 点击时同样为黑色 (Active text color is black)
            font=("Consolas", 10, "bold"),
            relief=tk.FLAT,
            command=self._handle_send
        )
        self.send_btn.pack(side=tk.LEFT, padx=(0, 5), ipadx=10, ipady=3)

        # 清除记录按钮 (Clear Button)
        self.clear_btn = tk.Button(
            input_frame, text="Clear / 清除",
            bg="#e2e8f0",
            fg="black",               # 文本颜色为黑色 (Text color is black)
            activeforeground="black", # 点击时同样为黑色 (Active text color is black)
            font=("Consolas", 10, "bold"),
            relief=tk.FLAT,
            command=self._clear_chat
        )
        self.clear_btn.pack(side=tk.LEFT, ipadx=10, ipady=3)
        # ------------------------------------------------------------

        self.input_box.focus()

    def _append_message(self, role: str, text: str):
        """将消息追加到聊天显示框 (Append a message to the chat display)"""
        self.chat_display.config(state=tk.NORMAL)
        if role == "user":
            self.chat_display.insert(tk.END, f"\n🧑 You / 你:\n{text}\n", "user")
        elif role == "bot":
            self.chat_display.insert(tk.END, f"\n{self.config.name}:\n{text}\n", "bot")
        elif role == "system":
            self.chat_display.insert(tk.END, f"\n[System / 系统]: {text}\n", "system")
        elif role == "reasoning":
            self.chat_display.insert(tk.END, f"{text}\n", "reasoning")
            
        self.chat_display.see(tk.END)
        self.chat_display.config(state=tk.DISABLED)

    def _check_resizing_module(self, text: str) -> bool:
        """检查并执行隐藏的大小调整命令 (Check and execute easter egg resizing commands)"""
        text_lower = text.lower()
        if "maximize" in text_lower:
            try:
                self.state('zoomed') # Windows
            except tk.TclError:
                self.attributes('-zoomed', True) # Linux / Mac fallback
            self._append_message("system", "🪟 Window maximized / 窗口已最大化.")
            return True
            
        elif "make it bigger" in text_lower:
            width = self.winfo_width() + 150
            height = self.winfo_height() + 100
            self.geometry(f"{width}x{height}")
            self._append_message("system", f"🪟 Window enlarged to / 窗口已放大至 {width}x{height}.")
            return True
            
        else:
            match = re.search(r"set width to (\d+)", text_lower)
            if match:
                width = int(match.group(1))
                height = self.winfo_height()
                self.geometry(f"{width}x{height}")
                self._append_message("system", f"🪟 Width set to / 宽度已设置为 {width}.")
                return True
                
        return False

    def _handle_send(self, event=None):
        """处理发送动作 (Handle the send action)"""
        user_text = self.input_box.get()
        if not user_text.strip():
            return
            
        self.input_box.delete(0, tk.END)
        self._append_message("user", user_text)

        # 检查是否是调整窗口的特殊指令 (Check for resizing Easter Eggs)
        if self._check_resizing_module(user_text):
            return

        # 防止并发请求 (Prevent concurrent generation requests)
        if self._current_thread and self._current_thread.is_alive():
            return

        self._current_thread = threading.Thread(
            target=self._generate_response_thread, 
            args=(user_text,)
        )
        self._current_thread.daemon = True
        self._current_thread.start()

    def _generate_response_thread(self, prompt: str):
        """在后台线程中生成并显示AI回复 (Generate and show AI response in background thread)"""
        # 禁用输入以免打断 (Disable inputs during thinking)
        self.input_box.config(state=tk.DISABLED)
        self.send_btn.config(state=tk.DISABLED)
        self.clear_btn.config(state=tk.DISABLED)
        
        reply, reasoning = self.engine.get_reply(prompt)
        
        # 逐行输出推理过程 (Output reasoning trace line by line)
        if reasoning:
            for line in reasoning:
                self.after(0, self._append_message, "reasoning", line)
                time.sleep(0.4) # 模拟思考时间 (Simulate thinking time)
                
        self.after(0, self._append_message, "bot", reply)
        
        # 恢复输入 (Restore UI state)
        def restore_ui():
            self.input_box.config(state=tk.NORMAL)
            self.send_btn.config(state=tk.NORMAL)
            self.clear_btn.config(state=tk.NORMAL)
            self.input_box.focus()
            
        self.after(0, restore_ui)

    def _clear_chat(self):
        """清除所有聊天记录 (Clear chat history)"""
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.delete(1.0, tk.END)
        self.chat_display.config(state=tk.DISABLED)
        self._append_message("system", "Chat history cleared / 聊天记录已清除。")


if __name__ == "__main__":
    app = CatR1ChatApp()
    app.mainloop()

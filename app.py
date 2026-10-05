import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Speech to Text",
    page_icon="🎤",
    layout="centered"
)

st.title("🎤 Speech-to-Text")
st.write("Speak into your microphone and convert your speech into text.")

html_code = """
<!DOCTYPE html>
<html>
<head>
<style>
body {
    font-family: Arial;
    text-align: center;
    padding: 20px;
}

select, button {
    padding: 12px;
    margin: 10px;
    font-size: 16px;
}

button {
    cursor: pointer;
    border-radius: 8px;
    border: none;
}

#start {
    background-color: #4CAF50;
    color: white;
}

#clear {
    background-color: #f44336;
    color: white;
}

textarea {
    width: 90%;
    height: 180px;
    font-size: 18px;
    padding: 10px;
}
</style>
</head>

<body>

<h2>🎤 Speech Recognition</h2>

<label><b>Select Language:</b></label>

<select id="language">
    <option value="en-IN">English</option>
    <option value="kn-IN">Kannada</option>
    <option value="hi-IN">Hindi</option>
</select>

<br>

<button id="start" onclick="startSpeech()">
🎤 Start Speaking
</button>

<button id="clear" onclick="clearText()">
🗑️ Clear
</button>

<p id="status">Ready to speak...</p>

<textarea id="result" placeholder="Your speech will appear here..."></textarea>

<script>

function startSpeech() {

    const SpeechRecognition =
        window.SpeechRecognition ||
        window.webkitSpeechRecognition;

    if (!SpeechRecognition) {
        alert(
          "Speech Recognition is not supported. Please use Google Chrome."
        );
        return;
    }

    const recognition = new SpeechRecognition();

    recognition.lang =
        document.getElementById("language").value;

    recognition.continuous = false;
    recognition.interimResults = false;

    document.getElementById("status").innerHTML =
        "🎤 Listening... Please speak.";

    recognition.start();

    recognition.onresult = function(event) {

        const text =
            event.results[0][0].transcript;

        document.getElementById("result").value +=
            text + " ";

        document.getElementById("status").innerHTML =
            "✅ Text converted successfully!";
    };

    recognition.onerror = function(event) {

        document.getElementById("status").innerHTML =
            "❌ Error: " + event.error;
    };

    recognition.onend = function() {

        if (document.getElementById("status").innerHTML.includes("Listening")) {
            document.getElementById("status").innerHTML =
                "Ready to speak again.";
        }
    };
}

function clearText() {

    document.getElementById("result").value = "";

    document.getElementById("status").innerHTML =
        "Text cleared. Ready to speak.";
}

</script>

</body>
</html>
"""

components.html(html_code, height=600)

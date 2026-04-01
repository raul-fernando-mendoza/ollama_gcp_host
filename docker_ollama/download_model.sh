
nohup ollama serve > ollama.log 2>&1 &
echo "Waiting for process ollama to start..."


while !  pgrep -x ollama ; do
    sleep 1
done

echo "Process ollama has started."


ollama ls

#ollama pull gemma2:2b 
#ollama pull qwen3-coder:30b
ollama pull qwen3-coder:30b-a3b-q4_K_M
ollama pull qwen3-coder-next:q8_0

ollama ls

kill $(pidof ollama)
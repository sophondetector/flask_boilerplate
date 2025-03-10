const input = document.querySelector('input') as HTMLInputElement
const output = document.getElementById('output') as HTMLDivElement
const submitBut = document.getElementById('submit') as HTMLButtonElement

submitBut.addEventListener('click', async (event) => {
	output.innerHTML = ''
	const query = input.value
	if (!query) {
		console.log('NOTHING TO SUBMIT')
		output.textContent = 'NOTHING TO SUBMIT'
		return
	}

	const params = new URLSearchParams({ query })

	try {
		const resp = await fetch('/endpoint?' + params.toString())
		const respJson = await resp.json()
		const jsonText = respJson['text']
		output.textContent = jsonText
	} catch (err) {
		console.log(`ERROR: ${err}`)
	}
})


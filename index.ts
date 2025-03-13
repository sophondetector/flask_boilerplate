const input = document.querySelector('input') as HTMLInputElement
const output = document.getElementById('output') as HTMLDivElement
const submitBut = document.getElementById('submit') as HTMLButtonElement

submitBut.addEventListener('click', async (event) => {
	output.innerHTML = ''
	const query = input.value
	if (!query) {
		console.log('ERROR: Blank Submission')
		output.textContent = 'ERROR: Blank Submission'
		return
	}

	const params = new URLSearchParams({ query })

	try {
		const resp = await fetch('/endpoint?' + params.toString())
		const respJson = await resp.json()
		const jsonText = respJson['text']

		console.log(jsonText)

		for (const ite of jsonText) {
			const p = document.createElement('p')
			p.textContent = ite
			output.appendChild(p)
		}

	} catch (err) {
		console.log(`ERROR: ${err}`)
	}
})


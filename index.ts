const input = document.querySelector('input') as HTMLInputElement
const output = document.getElementById('output') as HTMLDivElement
const submitBut = document.getElementById('submit') as HTMLButtonElement


async function getUserInput(): Promise<void> {
	output.innerHTML = ''

	const query = input.value
	const params = new URLSearchParams({ query })

	try {
		const resp = await fetch('/endpoint?' + params.toString())
		const respJson = await resp.json()
		const jsonText = respJson['text']

		console.log(jsonText)

		for (const ite of jsonText) {
			const autoSelectIte = document.createElement('li')
			autoSelectIte.textContent = ite
			output.appendChild(autoSelectIte)
		}

	} catch (err) {
		console.log(`ERROR: ${err}`)
	}
}

const MIN_MILLIS = 500

//@ts-ignore
let lastTimeoutId = null

input.addEventListener('input', async (ev) => {

	//@ts-ignore
	clearTimeout(lastTimeoutId)
	lastTimeoutId = setTimeout(
		async () => await getUserInput(),
		MIN_MILLIS
	)

})

document.addEventListener('click', (ev) => {
	// if event target is a result put it in input
	// and console log it
})


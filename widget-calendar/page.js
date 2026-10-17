(() => {
    const imageDescriptions = {
        month: ['월간 캘린더 위젯에서 날짜와 일정을 한눈에 확인하는 화면', 'A month calendar widget showing dates and events'],
        week: ['한 주의 일정을 표시하는 캘린더 위젯', 'A calendar widget showing the week’s events'],
        today: ['선택한 날짜의 일정 목록을 보여주는 Android 위젯', 'An Android widget listing events for the selected date'],
        upcoming: ['다가오는 일정을 날짜별로 모아 보여주는 Android 위젯', 'An Android widget listing upcoming events by date'],
        dots: ['일정을 색상 점으로 표시한 위젯', 'A widget showing events as colored dots'],
        count: ['날짜별 일정 개수를 표시한 위젯', 'A widget showing the event count for each date']
    };
    const descriptions = {
        ko: '홈 화면에서 한 달의 흐름과 오늘의 일정을 한눈에. Widget Cal의 캘린더 위젯, 일정 관리, 음력과 D-Day를 만나보세요.',
        en: 'Your month and today’s plans, at a glance. Discover Widget Cal’s Home screen calendar widgets, device calendar events, lunar dates and D-Day.'
    };
    function setLanguage(language) {
        const lang = language === 'en' ? 'en' : 'ko';
        document.documentElement.lang = lang;
        document.title = lang === 'ko' ? 'Widget Cal — 홈 화면에 놓는 나의 달력' : 'Widget Cal — Your calendar, on your Home screen';
        document.querySelector('meta[name="description"]').content = descriptions[lang];
        document.querySelectorAll('[data-ko]').forEach(el => { el.hidden = lang !== 'ko'; });
        document.querySelectorAll('[data-en]').forEach(el => { el.hidden = lang !== 'en'; });
        document.querySelectorAll('[data-lang]').forEach(button => { button.setAttribute('aria-pressed', String(button.dataset.lang === lang)); });
        document.querySelectorAll('[data-image]').forEach(img => {
            img.src = `assets/${lang}-${img.dataset.image}.webp`;
            img.alt = imageDescriptions[img.dataset.image][lang === 'ko' ? 0 : 1];
        });
        document.querySelectorAll('[data-local-link]').forEach(link => { link.href = `${link.dataset.localLink}/${lang === 'ko' ? 'ko/' : ''}`; });
    }
    document.querySelectorAll('[data-lang]').forEach(button => {
        button.addEventListener('click', () => {
            const lang = button.dataset.lang;
            const url = new URL(window.location.href);
            url.searchParams.set('lang', lang);
            history.replaceState(null, '', url);
            setLanguage(lang);
        });
    });
    const requested = new URLSearchParams(window.location.search).get('lang');
    setLanguage(requested === 'ko' || requested === 'en' ? requested : ((navigator.language || '').toLowerCase().startsWith('ko') ? 'ko' : 'en'));
})();
